# Assignment 2 - Bayesian Network Reasoner

## Requirements
Install the following dependencies:
```commandline
pip install networkx matplotlib pgmpy pandas
```

## Running the Tests
All the tests can be found in the ``testing`` folder. They can be run 
with the command:
```commandline
python -m unittest discover testing
```

Alternatively, it is also possible to clone this repository and running
the tests in an IDE such as PyCharm.

## Reproducing the Experiments
As shown in the paper, two experiments were conducted and their 
results can be reproduced as follows. 

### Experiment 1: Ordering Heuristics
The test set consisted of binary tree shaped BNs of four different sizes.
The following command can be run to reproduce the results for each
BN size, respectively:
```commandline
python -m experiments.ExperimentOrdering run_ordering_100_tree_3
python -m experiments.ExperimentOrdering run_ordering_100_tree_7
python -m experiments.ExperimentOrdering run_ordering_100_tree_15
python -m experiments.ExperimentOrdering run_ordering_100_tree_31
```

### Experiment 2: Summing-out Methods
Similarly, the following commands can be run to reproduce the results
from the summing-out method experiment for each BN size, respectively:
```commandline
python -m experiments.ExperimentSummingOut run_sum_out_100_tree_3
python -m experiments.ExperimentSummingOut run_sum_out_100_tree_7
python -m experiments.ExperimentSummingOut run_sum_out_100_tree_15
python -m experiments.ExperimentSummingOut run_sum_out_100_tree_31
```

## Output
After running any of the command outlined above, the runtime for each iteration and its corresponding
statistics are printed. These are computed sequentially for each algorithm
involved in the experiment. As an example, the format of the output is as follows:
```
Running the min-degree ordering heuristic on a BN of size 7...
Run 1 => 0.05739s
Run 2 => 0.05937s
.
.
.
Run 100 => 0.05384s

Running min-fill ordering heuristic on a BN of size 7...
Run 1 => 0.05199s
Run 2 => 0.05347s
.
.
.
Run 100 => 0.0534s

Results for the min-degree ordering heuristic (size = 7):
{
   "mean": 0.05623,
   "std": 0.00313,
   "max": 0.07018,
   "min": 0.05205,
   "range": 0.01813
}

Results for the min-fill ordering heuristic (size = 7):
{
   "mean": 0.05578,
   "std": 0.00332,
   "max": 0.06873,
   "min": 0.05021,
   "range": 0.01852
}

```
