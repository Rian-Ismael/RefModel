## Precision and recall on Java code

We evaluated the precision and recall of RefModel using different foundation models and compared its performance with state-of-the-art tools, [RefDiff, RefactoringMiner and ReExtractor+](./results.csv)..

### RefModel using Phi4:14B

| Refactoring Type          |  TP |  FP |  FN | Precision | Recall |
|---------------------------|----:|----:|----:|----------:|-------:|
| **Total**                 |  34 |  29 |  10 |     54.0% |   77.3% |
| Extract Class             |   1 |   0 |   0 |    100.0% |  100.0% |
| Extract Interface         |   8 |   1 |   0 |     88.9% |  100.0% |
| Extract Superclass        |   2 |   0 |   0 |    100.0% |  100.0% |
| Inline Method             |   4 |   1 |   1 |     80.0% |   80.0% |
| Move Method               |   3 |   1 |   5 |     75.0% |   37.5% |
| Pull Up Field             |   1 |   3 |   1 |     25.0% |   50.0% |
| Pull Up Method            |   4 |   9 |   1 |     30.8% |   80.0% |
| Push Down Field           |   1 |   3 |   0 |     25.0% |  100.0% |
| Push Down Method          |   2 |   0 |   2 |    100.0% |   50.0% |
| Rename Class              |   4 |   0 |   0 |    100.0% |  100.0% |
| Rename Field              |   1 |   0 |   0 |    100.0% |  100.0% |
| Rename Method             |   3 |   1 |   0 |     75.0% |  100.0% |


### RefModel using Gemini 2.5 Pro

| Refactoring Type         |  TP |  FP |  FN | Precision | Recall |
|--------------------------|----:|----:|----:|----------:|-------:|
| **Total**                |  40 |  12 |   4 |     76.9% |   90.9% |
| Extract Interface        |   6 |   0 |   2 |    100.0% |   75.0% |
| Extract Superclass       |   2 |   3 |   0 |     40.0% |  100.0% |
| Inline Method            |   5 |   0 |   0 |    100.0% |  100.0% |
| Move Method              |   8 |   1 |   0 |     88.9% |  100.0% |
| Pull Up Field            |   2 |   1 |   0 |     66.7% |  100.0% |
| Pull Up Method           |   4 |   3 |   1 |     57.1% |   80.0% |
| Push Down Field          |   1 |   1 |   0 |     50.0% |  100.0% |
| Push Down Method         |   4 |   0 |   0 |    100.0% |  100.0% |
| Rename Class             |   4 |   0 |   0 |    100.0% |  100.0% |
| Rename Field             |   1 |   1 |   0 |     50.0% |  100.0% |
| Rename Method            |   3 |   0 |   0 |    100.0% |  100.0% |


### RefModel using Claude 3.5 Sonnet

| Refactoring Type         |  TP |  FP |  FN | Precision | Recall |
|--------------------------|----:|----:|----:|----------:|-------:|
| **Total**                |  41 |  12 |   3 |     77.4% |   93.2% |
| Extract Interface        |   8 |   0 |   0 |    100.0% |  100.0% |
| Extract Superclass       |   2 |   1 |   0 |     66.7% |  100.0% |
| Inline Method            |   5 |   0 |   0 |    100.0% |  100.0% |
| Move Method              |   8 |   5 |   0 |     61.5% |  100.0% |
| Pull Up Field            |   2 |   2 |   0 |     50.0% |  100.0% |
| Pull Up Method           |   4 |   1 |   1 |     80.0% |   80.0% |
| Push Down Field          |   1 |   0 |   0 |    100.0% |  100.0% |
| Push Down Method         |   3 |   1 |   1 |     75.0% |   75.0% |
| Rename Class             |   4 |   0 |   0 |    100.0% |  100.0% |
| Rename Field             |   1 |   1 |   0 |     50.0% |  100.0% |
| Rename Method            |   3 |   0 |   0 |    100.0% |  100.0% |


### RefModel using o4-mini-high

| Refactoring Type         |  TP |  FP |  FN | Precision | Recall |
|--------------------------|----:|----:|----:|----------:|-------:|
| **Total**                |  41 |  10 |   3 |     80.4% |   93.2% |
| Extract Interface        |   8 |   0 |   0 |    100.0% |  100.0% |
| Extract Superclass       |   2 |   1 |   0 |     66.7% |  100.0% |
| Inline Method            |   4 |   1 |   1 |     80.0% |   80.0% |
| Move Method              |   7 |   0 |   1 |    100.0% |   87.5% |
| Pull Up Field            |   2 |   1 |   0 |     66.7% |  100.0% |
| Pull Up Method           |   5 |   4 |   0 |     55.6% |  100.0% |
| Push Down Field          |   1 |   0 |   0 |    100.0% |  100.0% |
| Push Down Method         |   4 |   0 |   0 |    100.0% |  100.0% |
| Rename Class             |   4 |   0 |   0 |    100.0% |  100.0% |
| Rename Field             |   1 |   1 |   0 |     50.0% |  100.0% |
| Rename Method            |   3 |   0 |   0 |    100.0% |  100.0% |