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
The test consisted of binary shaped BNs of four different sizes.
The following files can be run to reproduce the results for each
BN size, respectively:
```commandline
python -m experiments.ExperimentOrdering run_ordering_100_tree_3
python -m experiments.ExperimentOrdering run_ordering_100_tree_7
python -m experiments.ExperimentOrdering run_ordering_100_tree_15
python -m experiments.ExperimentOrdering run_ordering_100_tree_31
```

### Experiment 2: Summing-out Methods
Similarly, the following files can be run to reproduce the results
from the summing-out method experiment:
```commandline
python -m experiments.ExperimentSummingOut run_sum_out_100_tree_3
python -m experiments.ExperimentSummingOut run_sum_out_100_tree_7
python -m experiments.ExperimentSummingOut run_sum_out_100_tree_15
python -m experiments.ExperimentSummingOut run_sum_out_100_tree_31
```