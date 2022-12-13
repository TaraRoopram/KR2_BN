import unittest
import timeit

from BNReasoner import BNReasoner
from BayesNet import BayesNet
import BNReasonerUtil as util

ROUND_NUM = 5

class ExperimentSummingOutBinaryTree3(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("./bin_tree_3.BIFXML")
        self.reasoner = BNReasoner(self.bn)
        self.bn_size = 3

    def test_naive_summing_out_bin_tree_3(self):
        cpts_df = [cpt for cpt in self.bn.get_all_cpts().values()]
        cpts_name = [cpt for cpt in self.bn.get_all_cpts().keys()]
        multiplied = self.reasoner.n_f_multiplication(cpts_df)

        start = timeit.default_timer()
        summed_out = self.reasoner.marginalize(multiplied, [cpts_name[0]])
        for name in cpts_name[1:]:
            summed_out = self.reasoner.marginalize(summed_out, [name])
        stop = timeit.default_timer()

        print_experiment_results(name="summing out", type="naive",
                                 bn_size=self.bn_size, runtime=round(stop - start, ROUND_NUM))


class ExperimentSummingOutBinaryTree7(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("./bin_tree_7.BIFXML")
        self.reasoner = BNReasoner(self.bn)
        self.bn_size = 7

    def test_naive_summing_out_bin_tree_7(self):
        cpts_df = [cpt for cpt in self.bn.get_all_cpts().values()]
        cpts_name = [cpt for cpt in self.bn.get_all_cpts().keys()]
        multiplied = self.reasoner.n_f_multiplication(cpts_df)

        start = timeit.default_timer()
        summed_out = self.reasoner.marginalize(multiplied, [cpts_name[0]])
        for name in cpts_name[1:]:
            summed_out = self.reasoner.marginalize(summed_out, [name])
        stop = timeit.default_timer()

        print_experiment_results(name="summing out", type="naive",
                                 bn_size=self.bn_size, runtime=round(stop - start, ROUND_NUM))


class ExperimentSummingOutBinaryTree15(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("./bin_tree_15.BIFXML")
        self.reasoner = BNReasoner(self.bn)
        self.bn_size = 15

    def test_naive_summing_out_bin_tree_15(self):
        cpts_df = [cpt for cpt in self.bn.get_all_cpts().values()]
        cpts_name = [cpt for cpt in self.bn.get_all_cpts().keys()]
        multiplied = self.reasoner.n_f_multiplication(cpts_df)

        start = timeit.default_timer()
        summed_out = self.reasoner.marginalize(multiplied, [cpts_name[0]])
        for name in cpts_name[1:]:
            summed_out = self.reasoner.marginalize(summed_out, [name])
        stop = timeit.default_timer()

        print_experiment_results(name="summing out", type="naive",
                                 bn_size=self.bn_size, runtime=round(stop - start, ROUND_NUM))


class ExperimentSummingOutBinaryTree31(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("./bin_tree_31.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    # def test_naive_summing_out_bin_tree_31(self):
    #     cpts = [cpt for cpt in self.bn.get_all_cpts().values()]
    #     multiplied = self.reasoner.n_f_multiplication(cpts)
    #     print(multiplied)


def print_experiment_results(name="N/A", type="N/A", bn_size=-1, runtime=-1.):
    print(f"name: {name}")
    print(f"type: {type}")
    print(f"bn_size: {bn_size}")
    print(f"runtime: {runtime}")

