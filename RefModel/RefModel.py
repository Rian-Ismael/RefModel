#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import threading
import time
from datetime import date
from typing import Optional

import pandas as pd
import requests
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


DEFAULT_ANTHROPIC_API_KEY = ""

try:
    from dotenv import load_dotenv

    load_dotenv()
except ModuleNotFoundError:
    pass


P1 = "{program1}"
P2 = "{program2}"
PDIFF = "{diff}"


def ensure_ollama(cmd: str = "ollama") -> None:
    """Ensure the Ollama CLI is on your PATH; otherwise, display a tip."""
    if shutil.which(cmd):
        return

    hint = {
        "Linux": "curl -fsSL https://ollama.com/install.sh | sh",
    }.get(platform.system(), "See https://ollama.com/ for instructions")

    sys.exit(
        f"Ollama CLI not found.\n"
        f"Suggested installation:\n\n   {hint}\n"
    )


def start_ollama() -> None:
    """Starts ollama serve in the background if it's not already running."""
    def _run():
        os.environ["OLLAMA_HOST"] = "0.0.0.0:11434"
        os.environ["OLLAMA_ORIGINS"] = "*"
        subprocess.Popen(
            ["ollama", "serve"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    threading.Thread(target=_run, daemon=True).start()
    time.sleep(1)


def call_claude(
    prompt: str,
    model: str,
    api_key: str,
    temperature: float,
    max_tokens: int = 1024,
    api_url: str = "https://api.anthropic.com/v1/messages",
    timeout: int = 180,
) -> str:
    """Sends a prompt to the Claude API and returns the response."""
    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }
    data = {
        "model": model,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "messages": [{"role": "user", "content": prompt}],
    }
    resp = requests.post(api_url, headers=headers, json=data, timeout=timeout)
    try:
        resp.raise_for_status()
    except requests.HTTPError:
        sys.exit(f"Claude API error {resp.status_code}: {resp.text}")
    return resp.json()["content"][0]["text"]


def build_template(mode: str, ref_def: str) -> PromptTemplate:
    """
    Builds the full (uncut) prompt for both modes:
        • 'complete' → receives original + transformed program
        • 'diff'     → receives only the commit diff
    The text is 100% identical to the one used in your original script.
    """
    if mode == "complete":
        txt = f"""You are an expert coding assistant specialized in software refactoring, with many years of experience analyzing code transformations.

You will be given two versions of a program:

- **Original Version:**
{P1}

- **Transformed Version:**
{P2}

Your task is to identify which refactoring type(s) have been applied in transforming the original program into the new version. Use only the following list of predefined refactorings:

{ref_def}

**Instructions:**
1. Begin your response with a bullet-point list of the refactoring type(s) applied.
2. Then, briefly justify each identified refactoring with reference to the specific code changes.
3. Only include refactorings from the list above.
4. Be concise but precise in your explanations.

Do not generate explanations unrelated to the given transformation."""
        return PromptTemplate(
            input_variables=["program1", "program2"],
            template=txt,
        )

    txt = f"""You are an expert coding assistant specialized in software refactoring, with many years of experience analyzing code transformations.

You will be given the diffs of a commit:

- **Diffs:**
{PDIFF}

Your task is to identify which refactoring type(s) have been applied in transforming the original program into the new version. Use only the following list of predefined refactorings:

{ref_def}

**Instructions:**
1. Begin your response with a bullet-point list of the refactoring type(s) applied.
2. Then, briefly justify each identified refactoring with reference to the specific code changes.
3. Only include refactorings from the list above.
4. Be concise but precise in your explanations.

Do not generate explanations unrelated to the transformation."""
    return PromptTemplate(
        input_variables=["diff"],
        template=txt,
    )


def main() -> None:
    ap = argparse.ArgumentParser("Detect refactorings via LLM")
    ap.add_argument("--backend", choices=["ollama", "claude"], default="ollama")
    ap.add_argument("--mode", choices=["complete", "diff"], required=True)
    ap.add_argument("--csv", required=True)
    ap.add_argument("--definitions", default="refactoring_definitions.txt")
    
    backend_default = "phi4" if "--backend ollama" in sys.argv else "claude-3-5-sonnet-20241022"
    ap.add_argument("--model", default=backend_default)
    ap.add_argument("--temperature", type=float, default=0.6)
    ap.add_argument("--base_url", default="http://localhost:11434")
    ap.add_argument("--api_key", default=None)
    ap.add_argument("--max_tokens", type=int, default=1024)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    if not os.path.isfile(args.definitions):
        sys.exit(f"{args.definitions} not found")
    with open(args.definitions, encoding="utf-8") as f:
        ref_def = f.read().strip()

    prompt_template = build_template(args.mode, ref_def)

    if args.backend == "ollama":
        ensure_ollama()
        start_ollama()
        subprocess.run(["ollama", "pull", args.model], check=True)

        llm = OllamaLLM(
            model=args.model,
            base_url=args.base_url,
            temperature=args.temperature,
        )
        chain = LLMChain(llm=llm, prompt=prompt_template)

        def run_llm(**kw: str) -> str:
            return chain.run(**kw)

    else:
        api_key = (
            args.api_key
            or os.getenv("ANTHROPIC_API_KEY")
            or DEFAULT_ANTHROPIC_API_KEY
        )
        if not api_key:
            sys.exit(
                "Claude backend selected, but no API key was provided.\n"
                "Use --api_key, define ANTHROPIC_API_KEY, or fill in DEFAULT_ANTHROPIC_API_KEY."
            )

        def run_llm(**kw: str) -> str:
            prompt = prompt_template.format(**kw)
            return call_claude(
                prompt, args.model, api_key, args.temperature, args.max_tokens
            )

    df = pd.read_csv(args.csv)
    today = date.today()
    out_csv = args.out or f"results-{args.mode}-{args.backend}-{args.model}.csv"

    if args.mode == "complete":
        for idx in range(len(df)):
            res = run_llm(
                program1=df.at[idx, "input"],
                program2=df.at[idx, "output"],
            )
            df.at[idx, "LLM"] = args.model
            df.at[idx, "Date"] = today
            df.at[idx, "LLM Output"] = res
    else:
        for idx in range(len(df)):
            res = run_llm(diff=df.at[idx, "diff"])
            df.at[idx, "LLM"] = args.model
            df.at[idx, "Date"] = today
            df.at[idx, "LLM Output"] = res

    df.to_csv(out_csv, index=False)
    print(f"Results saved to: {out_csv}")


if __name__ == "__main__":
    main()
