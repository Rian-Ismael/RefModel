## Precision and recall

We evaluated the precision and recall of RefModel using different foundation models and compared its performance with state-of-the-art tool [RefactoringMiner](./results.csv).

### RefModel using Phi4:14B

| Refactoring Type                         |  TP |  FP |  FN | Precision | Recall |
|------------------------------------------|----:|----:|----:|----------:|-------:|
| **Total**                                | 681 | 526 | 177 |     56.4% |   79.4% |
| Add Method Parameter                     |  97 |   2 |   3 |     98.0% |   97.0% |
| Encapsulate Field                        | 100 |  11 |   0 |     90.1% |  100.0% |
| Move Method                              |  54 |  35 |  46 |     60.7% |   54.0% |
| Pull Up Field                            |  85 | 181 |  15 |     32.0% |   85.0% |
| Pull Up Method                           |  38 | 127 |   9 |     23.0% |   80.9% |
| Push Down Field                          |  52 |  23 |  48 |     69.3% |   52.0% |
| Push Down Method                         |   1 |  33 |  10 |      2.9% |    9.1% |
| Rename Class                             |  90 |   0 |  10 |    100.0% |   90.0% |
| Rename Field                             |  65 |   2 |  35 |     97.0% |   65.0% |
| Rename Method                            |  99 |   9 |   1 |     91.7% |   99.0% |


### RefModel using Claude 3.5 Sonnet

| Refactoring Type                         |  TP |  FP |  FN | Precision | Recall |
|------------------------------------------|----:|----:|----:|----------:|-------:|
| **Total**                                | 845 | 110 |  13 |     88.5% |   98.5% |
| Add Method Parameter                     | 100 |  13 |   0 |     88.5% |  100.0% |
| Encapsulate Field                        | 100 |   2 |   0 |     98.0% |  100.0% |
| Move Method                              |  93 |   5 |   7 |     94.9% |   93.0% |
| Pull Up Field                            | 100 |  13 |   0 |     88.5% |  100.0% |
| Pull Up Method                           |  45 |   2 |   2 |     95.7% |   95.7% |
| Push Down Field                          | 100 |   3 |   0 |     97.1% |  100.0% |
| Push Down Method                         |   9 |  15 |   2 |     37.5% |   81.8% |
| Rename Class                             |  99 |   0 |   1 |    100.0% |   99.0% |
| Rename Field                             |  99 |   0 |   1 |    100.0% |   99.0% |
| Rename Method                            | 100 |   1 |   0 |     99.0% |  100.0% |

