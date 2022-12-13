import json
import unittest
import timeit
from typing import Union, List

from BNReasoner import BNReasoner
from BayesNet import BayesNet
import BNReasonerUtil as util

ROUND_NUM = 5
ITERATIONS = 5


class ExperimentOrderingBinaryTree3(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("./bin_tree_3.BIFXML")
        self.reasoner = BNReasoner(self.bn)
        self.bn_size = 3

    def test_min_deg_bin_tree_3(self):
        factors = self.bn.get_all_cpts()
        variables = self.bn.get_all_variables()
        runtime = perform_min_deg(self.reasoner, factors, variables)

        print_experiment_results(name="ordering", type="min_deg", bn_size=self.bn_size, runtime=runtime)

    def test_min_fill_bin_tree_3(self):
        factors = self.bn.get_all_cpts()
        variables = self.bn.get_all_variables()
        runtime = perform_min_fill(self.reasoner, factors, variables)

        print_experiment_results(name="ordering", type="min_fill", bn_size=self.bn_size, runtime=runtime)

    def test_100_min_deg_bin_tree_3(self):
        factors = self.bn.get_all_cpts()
        variables = self.bn.get_all_variables()
        all_runtime = perform_100_min_deg(self.reasoner, factors, variables)

        print_experiment_results(name="ordering", type="min_deg",
                                 bn_size=self.bn_size, runtime=all_runtime)
        save_experiment_results(f"bin_tree_{self.bn_size}_min_deg_{ITERATIONS}.json",
                                name="ordering", type="min_deg",
                                bn_size=self.bn_size, runtime=all_runtime)

    def test_100_min_fill_bin_tree_3(self):
        factors = self.bn.get_all_cpts()
        variables = self.bn.get_all_variables()
        all_runtime = perform_100_min_fill(self.reasoner, factors, variables)

        print_experiment_results(name="ordering", type="min_fill",
                                 bn_size=self.bn_size, runtime=all_runtime)
        save_experiment_results(f"bin_tree_{self.bn_size}_min_fill_{ITERATIONS}.json",
                                name="ordering", type="min_fill",
                                bn_size=self.bn_size, runtime=all_runtime)


class ExperimentOrderingBinaryTree7(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("./bin_tree_7.BIFXML")
        self.reasoner = BNReasoner(self.bn)
        self.bn_size = 7

    def test_min_deg_bin_tree_7(self):
        factors = self.bn.get_all_cpts()
        variables = self.bn.get_all_variables()
        runtime = perform_min_deg(self.reasoner, factors, variables)

        print_experiment_results(name="ordering", type="min_deg", bn_size=self.bn_size, runtime=runtime)

    def test_min_fill_bin_tree_7(self):
        factors = self.bn.get_all_cpts()
        variables = self.bn.get_all_variables()
        runtime = perform_min_fill(self.reasoner, factors, variables)

        print_experiment_results(name="ordering", type="min_fill", bn_size=self.bn_size, runtime=runtime)

    def test_100_min_deg_bin_tree_7(self):
        factors = self.bn.get_all_cpts()
        variables = self.bn.get_all_variables()
        all_runtime = perform_100_min_deg(self.reasoner, factors, variables)

        print_experiment_results(name="ordering", type="min_deg",
                                 bn_size=self.bn_size, runtime=all_runtime)
        save_experiment_results(f"bin_tree_{self.bn_size}_min_deg_{ITERATIONS}.json",
                                name="ordering", type="min_deg",
                                bn_size=self.bn_size, runtime=all_runtime)

    def test_100_min_fill_bin_tree_7(self):
        factors = self.bn.get_all_cpts()
        variables = self.bn.get_all_variables()
        all_runtime = perform_100_min_fill(self.reasoner, factors, variables)

        print_experiment_results(name="ordering", type="min_fill",
                                 bn_size=self.bn_size, runtime=all_runtime)
        save_experiment_results(f"bin_tree_{self.bn_size}_min_fill_{ITERATIONS}.json",
                                name="ordering", type="min_fill",
                                bn_size=self.bn_size, runtime=all_runtime)


class ExperimentOrderingBinaryTree15(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("./bin_tree_15.BIFXML")
        self.reasoner = BNReasoner(self.bn)
        self.bn_size = 15

    def test_min_deg_bin_tree_15(self):
        factors = self.bn.get_all_cpts()
        variables = self.bn.get_all_variables()
        runtime = perform_min_deg(self.reasoner, factors, variables)

        print_experiment_results(name="ordering", type="min_deg", bn_size=self.bn_size, runtime=runtime)

    def test_min_fill_bin_tree_15(self):
        factors = self.bn.get_all_cpts()
        variables = self.bn.get_all_variables()
        runtime = perform_min_fill(self.reasoner, factors, variables)

        print_experiment_results(name="ordering", type="min_fill", bn_size=self.bn_size, runtime=runtime)

    def test_100_min_deg_bin_tree_15(self):
        factors = self.bn.get_all_cpts()
        variables = self.bn.get_all_variables()
        all_runtime = perform_100_min_deg(self.reasoner, factors, variables)

        print_experiment_results(name="ordering", type="min_deg",
                                 bn_size=self.bn_size, runtime=all_runtime)
        save_experiment_results(f"bin_tree_{self.bn_size}_min_deg_{ITERATIONS}.json",
                                name="ordering", type="min_deg",
                                bn_size=self.bn_size, runtime=all_runtime)

    def test_100_min_fill_bin_tree_15(self):
        factors = self.bn.get_all_cpts()
        variables = self.bn.get_all_variables()
        all_runtime = perform_100_min_fill(self.reasoner, factors, variables)

        print_experiment_results(name="ordering", type="min_fill",
                                 bn_size=self.bn_size, runtime=all_runtime)
        save_experiment_results(f"bin_tree_{self.bn_size}_min_fill_{ITERATIONS}.json",
                                name="ordering", type="min_fill",
                                bn_size=self.bn_size, runtime=all_runtime)


class ExperimentOrderingBinaryTree31(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("./bin_tree_31.BIFXML")
        self.reasoner = BNReasoner(self.bn)
        self.bn_size = 31

    def test_min_deg_bin_tree_31(self):
        factors = self.bn.get_all_cpts()
        variables = self.bn.get_all_variables()
        runtime = perform_min_deg(self.reasoner, factors, variables)

        print_experiment_results(name="ordering", type="min_deg", bn_size=self.bn_size, runtime=runtime)

    def test_min_fill_bin_tree_31(self):
        factors = self.bn.get_all_cpts()
        variables = self.bn.get_all_variables()
        runtime = perform_min_fill(self.reasoner, factors, variables)

        print_experiment_results(name="ordering", type="min_fill", bn_size=self.bn_size, runtime=runtime)

    def test_100_min_deg_bin_tree_31(self):
        factors = self.bn.get_all_cpts()
        variables = self.bn.get_all_variables()
        all_runtime = perform_100_min_deg(self.reasoner, factors, variables)

        print_experiment_results(name="ordering", type="min_deg",
                                 bn_size=self.bn_size, runtime=all_runtime)
        save_experiment_results(f"bin_tree_{self.bn_size}_min_deg_{ITERATIONS}.json",
                                name="ordering", type="min_deg",
                                bn_size=self.bn_size, runtime=all_runtime)

    def test_100_min_fill_bin_tree_31(self):
        factors = self.bn.get_all_cpts()
        variables = self.bn.get_all_variables()
        all_runtime = perform_100_min_fill(self.reasoner, factors, variables)

        print_experiment_results(name="ordering", type="min_fill",
                                 bn_size=self.bn_size, runtime=all_runtime)
        save_experiment_results(f"bin_tree_{self.bn_size}_min_fill_{ITERATIONS}.json",
                                name="ordering", type="min_fill",
                                bn_size=self.bn_size, runtime=all_runtime)


def perform_min_fill(reasoner: BNReasoner, factors, variables):
    start = timeit.default_timer()
    min_fill = reasoner.compute_ordering_min_fill(variables)
    var_elim = reasoner.variable_elimination(factors, min_fill)
    stop = timeit.default_timer()
    return round(stop - start, ROUND_NUM)


def perform_min_deg(reasoner: BNReasoner, factors, variables):
    start = timeit.default_timer()
    min_fill = reasoner.compute_ordering_min_deg(variables)
    var_elim = reasoner.variable_elimination(factors, min_fill)
    stop = timeit.default_timer()
    return round(stop - start, ROUND_NUM)


def perform_100_min_deg(reasoner: BNReasoner, factors, variables):
    all_runtime = []
    for i in range(ITERATIONS):
        print(i)
        runtime = perform_min_deg(reasoner, factors, variables)
        all_runtime.append(runtime)

    return all_runtime


def perform_100_min_fill(reasoner: BNReasoner, factors, variables):
    all_runtime = []
    for i in range(ITERATIONS):
        print(i)
        runtime = perform_min_fill(reasoner, factors, variables)
        all_runtime.append(runtime)

    return all_runtime


def print_experiment_results(name="N/A", type="N/A", bn_size=-1, runtime: Union[float, List[float]] = -1.):
    print(f"name: {name}")
    print(f"type: {type}")
    print(f"bn_size: {bn_size}")
    print(f"runtime: {runtime}")


def save_experiment_results(filename, name="N/A", type="N/A", bn_size=-1, runtime: Union[float, List[float]] = -1.):
    result = {
        "name": name,
        "type": type,
        "bn_size": bn_size,
        "runtime": runtime
    }

    with open(f"./results/{filename}", "w+") as file:
        json.dump(result, file, indent=3)
