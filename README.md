# RefModel

### About 
RefModel is a tool that leverages foundation models to automatically detect code refactoring operations in program transformations. By default, it analyzes both the original and transformed versions of a program to identify refactorings. However, when dealing with large programs that exceed the model’s context window, RefModel can alternatively operate by analyzing only the code differences (diffs) introduced by the transformation.

---

## Contents
This repository contains the source code, datasets, and results related to the model evaluations:

- **Demonstrations** – [`docs/`](./docs/)  
  Visual assets including GIFs and videos that demonstrate how the model works in both Full and Small Programs and Diffs of Large Programs.
  
- **Usage Instructions** – [`RefModel/`](./RefModel)
  Step-by-step guides on how to use the model.

- **Dataset** – [`dataset/`](./dataset/)
Contains  the full datasets used in the evaluation: Full and Small Programs and Diffs of Large Programs.

- **Performance Results** – [`evaluation/`](./evaluation/)
Contains  precision and recall metrics using different models. We compare the results of our RefModel against tools like RefactoringMiner, RefDiff, and ReExtractor+ across both datasets.
---

### Currently Supported Refactorings
RefModel currently supports 19 distinct refactoring types, with an architecture designed for easy extension by simply adding a natural language definition for each new refactoring in a text file.

1. **Add Method Parameter**  
2. **Remove Method Parameter**  
3. **Rename Method**  
4. **Rename Class**  
5. **Rename Package**  
6. **Rename Field**  
7. **Extract Class**  
8. **Extract Superclass**  
9. **Inline Method**  
10. **Pull Up Method**  
11. **Push Down Method**  
12. **Pull Up Field**  
13. **Push Down Field**  
14. **Inline Class**  
15. **Extract Interface**  
16. **Move Method**  
17. **Move Field**  
18. **Replace Magic Number with Constant**  
19. **Encapsulate Field**

---

## How to Run RefModel

You can run `RefModel` in two ways:

* **Terminal**: Use the command-line script located in [`./RefModel`](./RefModel).
* **Notebook**: Use the Colab notebook available in [`./RefModel/notebook`](./RefModel/notebook).

---

# Research
## How to cite RefactoringMiner
If you are using RefModel in your research, please cite the following paper:

```bibtex
@inproceedings{refModel2025,
  author    = {Pedro Simões and Rohit Gheyi and Rian Melo and Jonhnanthan Oliveira and Márcio Ribeiro and Wesley K. G. Assunção},
  title     = {RefModel: Detecting Refactorings using Foundation Models},
  booktitle = {Brazilian Symposium on Software Engineering},
  year      = {2025},
  url       = {https://arxiv.org/abs/2507.11346}
}
```

### Structure summary

The structure is shown below:

## Directory tree

```text
├── dataset/                                   # CSV datasets used as input
│   ├── full-and-small-programs.csv            # dataset Full and Small Programs
│   └── diff-of-large-programs.csv             # dataset Diff of Large Programs
│
├── docs/                                      # Visual documentation and demo media
│   ├── full-and-small-programs.gif            # GIF – Full & Small Programs
│   ├── diff-of-large-programs.gif             # GIF – Diffs of Large Programs
│   ├── full-and-small-programs.mp4            # video – Full & Small Programs
│   └── diff-of-large-programs.mp4             # video – Diffs of Large Programs
│
├── evaluation/                                # Evaluation outputs from models
│   ├── full-and-small-programs/               # Metrics for full and small programs
│   │   └── results.csv                        # Precision/recall for each model
│   │
│   └── diff-of-large-programs/                # Metrics for large diff-only programs
│       ├── golang/                            # Go language
│       │   ├── gemini-2.5-pro.pdf             # Gemini 2.5 Pro results
│       │   └── o4-mini-high.pdf               # O4-mini-high results
│       │
│       ├── java/                              # Java language
│       │   ├── gemini-2.5-pro.pdf             # Gemini 2.5 Pro results
│       │   └── o4-mini-high.pdf               # O4-mini-high results
│       │
│       ├── python/                            # Python language
│       │   ├── gemini-2.5-pro.pdf             # Gemini 2.5 Pro results
│       │   └── o4-mini-high.pdf               # O4-mini-high results
│       │
│       └── results.csv                        # Aggregated metrics across all models
│
├── RefModel/                                  # Main source code and configuration
│   ├── RefModel.py                            # Core script to run the tool
│   ├── notebook/
│   │   └── RefModel.ipynb                     # notebook
│   │
│   ├── requirements.txt                       # Required Python dependencies
│   ├── README.md                              # Documentation for the RefModel module
│   │
│   ├── resources/                             # definitions
│   │   └── refactoring_definitions.txt        # List of predefined refactoring types
│   │
│   └── data/                                  # Folder for generated I/O files
│       ├── input/                             # CSV files to be processed
│       │   └── your.csv                       # Example input file
│       │
│       └── output/                            # Output results from execution
│
├── README.md                                  # Project overview and instructions
└── .gitignore                                 # Files ignored by Git

```

### Running

The screencast below shows the process running:

### Running: Full and Small Programs

The following screencast demonstrates how to use RefModel to analyze both the original and transformed versions of a small program to detect refactorings.

![how to run 'complete'](docs/full-and-small-programs-ollama.gif)

### Running: Diff of Large Programs

The following screencast demonstrates how to use RefModel to analyze the code differences (diffs) introduced by transformations applied to larger programs.

![how to run 'diff'](docs/diff-of-large-programs-claude.gif)
