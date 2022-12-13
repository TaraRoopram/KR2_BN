import unittest
import timeit
import json
from typing import Union, List

from BNReasoner import BNReasoner
from BayesNet import BayesNet
import BNReasonerUtil as util

ROUND_NUM = 5
ITERATIONS = 100


class ExperimentSummingOutBinaryTree3(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("./bin_tree_3.BIFXML")
        self.reasoner = BNReasoner(self.bn)
        self.bn_size = 3

    def test_naive_summing_out_bin_tree_3(self):
        runtime = perform_naive_sum_out(self.bn, self.reasoner)
        print_experiment_results(name="summing out", type="naive",
                                 bn_size=self.bn_size, runtime=runtime)

    def test_var_elim_bin_tree_3(self):
        runtime = perform_var_elim(self.bn, self.reasoner)
        print_experiment_results(name="summing out", type="var_elim",
                                 bn_size=self.bn_size, runtime=runtime)

    def test_100_naive_summing_out_bin_tree_3(self):
        all_runtime = []
        for i in range(ITERATIONS):
            runtime = perform_naive_sum_out(self.bn, self.reasoner)
            all_runtime.append(runtime)

        print_experiment_results(name="summing out", type="naive",
                                 bn_size=self.bn_size, runtime=all_runtime)
        save_experiment_results(f"bin_tree_{self.bn_size}_naive_{ITERATIONS}.json",
                                name="summing out", type="naive",
                                bn_size=self.bn_size, runtime=all_runtime)

    def test_100_var_elim_bin_tree_3(self):
        all_runtime = []
        for i in range(ITERATIONS):
            runtime = perform_var_elim(self.bn, self.reasoner)
            all_runtime.append(runtime)

        print_experiment_results(name="summing out", type="var_elim",
                                 bn_size=self.bn_size, runtime=all_runtime)
        save_experiment_results(f"bin_tree_{self.bn_size}_var_elim_{ITERATIONS}.json",
                                name="summing out", type="var_elim",
                                bn_size=self.bn_size, runtime=all_runtime)


class ExperimentSummingOutBinaryTree7(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("./bin_tree_7.BIFXML")
        self.reasoner = BNReasoner(self.bn)
        self.bn_size = 7

    def test_naive_summing_out_bin_tree_7(self):
        runtime = perform_naive_sum_out(self.bn, self.reasoner)
        print_experiment_results(name="summing out", type="naive",
                                 bn_size=self.bn_size, runtime=runtime)

    def test_var_elim_bin_tree_7(self):
        runtime = perform_var_elim(self.bn, self.reasoner)
        print_experiment_results(name="summing out", type="var_elim",
                                 bn_size=self.bn_size, runtime=runtime)

    def test_100_naive_summing_out_bin_tree_7(self):
        all_runtime = []
        for i in range(ITERATIONS):
            runtime = perform_naive_sum_out(self.bn, self.reasoner)
            all_runtime.append(runtime)

        print_experiment_results(name="summing out", type="naive",
                                 bn_size=self.bn_size, runtime=all_runtime)
        save_experiment_results(f"bin_tree_{self.bn_size}_naive_{ITERATIONS}.json",
                                name="summing out", type="naive",
                                bn_size=self.bn_size, runtime=all_runtime)

    def test_100_var_elim_bin_tree_7(self):
        all_runtime = []
        for i in range(ITERATIONS):
            runtime = perform_var_elim(self.bn, self.reasoner)
            all_runtime.append(runtime)

        print_experiment_results(name="summing out", type="var_elim",
                                 bn_size=self.bn_size, runtime=all_runtime)
        save_experiment_results(f"bin_tree_{self.bn_size}_var_elim_{ITERATIONS}.json",
                                name="summing out", type="var_elim",
                                bn_size=self.bn_size, runtime=all_runtime)


class ExperimentSummingOutBinaryTree15(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("./bin_tree_15.BIFXML")
        self.reasoner = BNReasoner(self.bn)
        self.bn_size = 15

    @unittest.skip
    def test_naive_summing_out_bin_tree_15(self):
        runtime = perform_naive_sum_out(self.bn, self.reasoner)
        print_experiment_results(name="summing out", type="naive",
                                 bn_size=self.bn_size, runtime=runtime)

    @unittest.skip
    def test_var_elim_bin_tree_15(self):
        runtime = perform_var_elim(self.bn, self.reasoner)
        print_experiment_results(name="summing out", type="var_elim",
                                 bn_size=self.bn_size, runtime=runtime)

    def test_100_naive_summing_out_bin_tree_15(self):
        all_runtime = []
        for i in range(ITERATIONS):
            runtime = perform_naive_sum_out(self.bn, self.reasoner)
            all_runtime.append(runtime)

        print_experiment_results(name="summing out", type="naive",
                                 bn_size=self.bn_size, runtime=all_runtime)
        save_experiment_results(f"bin_tree_{self.bn_size}_naive_{ITERATIONS}.json",
                                name="summing out", type="naive",
                                bn_size=self.bn_size, runtime=all_runtime)

    def test_100_var_elim_bin_tree_15(self):
        all_runtime = []
        for i in range(ITERATIONS):
            runtime = perform_var_elim(self.bn, self.reasoner)
            all_runtime.append(runtime)

        print_experiment_results(name="summing out", type="var_elim",
                                 bn_size=self.bn_size, runtime=all_runtime)
        save_experiment_results(f"bin_tree_{self.bn_size}_var_elim_{ITERATIONS}.json",
                                name="summing out", type="var_elim",
                                bn_size=self.bn_size, runtime=all_runtime)


class ExperimentSummingOutBinaryTree31(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("./bin_tree_31.BIFXML")
        self.reasoner = BNReasoner(self.bn)
        self.bn_size = 31

    @unittest.skip
    def test_naive_summing_out_bin_tree_31(self):
        runtime = perform_naive_sum_out(self.bn, self.reasoner)
        print_experiment_results(name="summing out", type="naive",
                                 bn_size=self.bn_size, runtime=runtime)

    @unittest.skip
    def test_var_elim_bin_tree_31(self):
        runtime = perform_var_elim(self.bn, self.reasoner)
        print_experiment_results(name="summing out", type="var_elim",
                                 bn_size=self.bn_size, runtime=runtime)

    def test_100_naive_summing_out_bin_tree_31(self):
        all_runtime = []
        for i in range(ITERATIONS):
            runtime = perform_naive_sum_out(self.bn, self.reasoner)
            all_runtime.append(runtime)

        print_experiment_results(name="summing out", type="naive",
                                 bn_size=self.bn_size, runtime=all_runtime)
        save_experiment_results(f"bin_tree_{self.bn_size}_naive_{ITERATIONS}.json",
                                name="summing out", type="naive",
                                bn_size=self.bn_size, runtime=all_runtime)

    def test_100_var_elim_bin_tree_31(self):
        all_runtime = []
        for i in range(ITERATIONS):
            runtime = perform_var_elim(self.bn, self.reasoner)
            all_runtime.append(runtime)

        print_experiment_results(name="summing out", type="var_elim",
                                 bn_size=self.bn_size, runtime=all_runtime)
        save_experiment_results(f"bin_tree_{self.bn_size}_var_elim_{ITERATIONS}.json",
                                name="summing out", type="var_elim",
                                bn_size=self.bn_size, runtime=all_runtime)


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


def perform_naive_sum_out(bn: BayesNet, reasoner: BNReasoner):
    cpts_df = [cpt for cpt in bn.get_all_cpts().values()]
    cpts_name = [cpt for cpt in bn.get_all_cpts().keys()]

    start = timeit.default_timer()
    multiplied = reasoner.n_f_multiplication(cpts_df)
    summed_out = reasoner.marginalize(multiplied, [cpts_name[0]])
    for name in cpts_name[1:]:
        summed_out = reasoner.marginalize(summed_out, [name])
    stop = timeit.default_timer()

    return round(stop - start, ROUND_NUM)


def perform_var_elim(bn: BayesNet, reasoner: BNReasoner):
    cpts_df = bn.get_all_cpts()
    cpts_name = [cpt for cpt in bn.get_all_cpts().keys()]

    start = timeit.default_timer()
    var_elim = reasoner.variable_elimination(cpts_df, cpts_name)
    stop = timeit.default_timer()

    return round(stop - start, ROUND_NUM)
