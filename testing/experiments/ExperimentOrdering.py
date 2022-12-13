import unittest
import timeit

from BNReasoner import BNReasoner
from BayesNet import BayesNet
import BNReasonerUtil as util


class ExperimentOrderingBinaryTree3(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("./bin_tree_3.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_min_deg_bin_tree_3(self):
        factors = self.bn.get_all_cpts()
        variables = self.bn.get_all_variables()

        start = timeit.default_timer()
        min_deg = self.reasoner.compute_ordering_min_deg(variables)
        var_elim = self.reasoner.variable_elimination(factors, min_deg)
        stop = timeit.default_timer()

        print_experiment_results({
            "name": "ordering",
            "type": "min_deg",
            "bn_size": 3,
            "runtime": round(stop - start, 2)
        })

    def test_min_fill_bin_tree_3(self):
        factors = self.bn.get_all_cpts()
        variables = self.bn.get_all_variables()

        start = timeit.default_timer()
        min_fill = self.reasoner.compute_ordering_min_fill(variables)
        var_elim = self.reasoner.variable_elimination(factors, min_fill)
        stop = timeit.default_timer()

        print_experiment_results({
            "name": "ordering",
            "type": "min_fill",
            "bn_size": 3,
            "runtime": round(stop - start, 2)
        })


class ExperimentOrderingBinaryTree7(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("./bin_tree_7.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_min_deg_bin_tree_7(self):
        factors = self.bn.get_all_cpts()
        variables = self.bn.get_all_variables()

        start = timeit.default_timer()
        min_deg = self.reasoner.compute_ordering_min_deg(variables)
        var_elim = self.reasoner.variable_elimination(factors, min_deg)
        stop = timeit.default_timer()

        print_experiment_results({
            "name": "ordering",
            "type": "min_deg",
            "bn_size": 7,
            "runtime": round(stop - start, 2)
        })

    def test_min_fill_bin_tree_7(self):
        factors = self.bn.get_all_cpts()
        variables = self.bn.get_all_variables()

        start = timeit.default_timer()
        min_fill = self.reasoner.compute_ordering_min_fill(variables)
        var_elim = self.reasoner.variable_elimination(factors, min_fill)
        stop = timeit.default_timer()

        print_experiment_results({
            "name": "ordering",
            "type": "min_fill",
            "bn_size": 7,
            "runtime": round(stop - start, 2)
        })


class ExperimentOrderingBinaryTree15(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("./bin_tree_15.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_min_deg_bin_tree_15(self):
        factors = self.bn.get_all_cpts()
        variables = self.bn.get_all_variables()

        start = timeit.default_timer()
        min_deg = self.reasoner.compute_ordering_min_deg(variables)
        var_elim = self.reasoner.variable_elimination(factors, min_deg)
        stop = timeit.default_timer()

        print_experiment_results({
            "name": "ordering",
            "type": "min_deg",
            "bn_size": 15,
            "runtime": round(stop - start, 2)
        })

    def test_min_fill_bin_tree_15(self):
        factors = self.bn.get_all_cpts()
        variables = self.bn.get_all_variables()

        start = timeit.default_timer()
        min_fill = self.reasoner.compute_ordering_min_fill(variables)
        var_elim = self.reasoner.variable_elimination(factors, min_fill)
        stop = timeit.default_timer()

        print_experiment_results({
            "name": "ordering",
            "type": "min_fill",
            "bn_size": 15,
            "runtime": round(stop - start, 2)
        })


class ExperimentOrderingBinaryTree31(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("./bin_tree_31.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_min_deg_bin_tree_31(self):
        factors = self.bn.get_all_cpts()
        variables = self.bn.get_all_variables()

        start = timeit.default_timer()
        min_deg = self.reasoner.compute_ordering_min_deg(variables)
        var_elim = self.reasoner.variable_elimination(factors, min_deg)
        stop = timeit.default_timer()

        print_experiment_results({
            "name": "ordering",
            "type": "min_deg",
            "bn_size": 31,
            "runtime": round(stop - start, 2)
        })

    def test_min_fill_bin_tree_31(self):
        factors = self.bn.get_all_cpts()
        variables = self.bn.get_all_variables()

        start = timeit.default_timer()
        min_fill = self.reasoner.compute_ordering_min_fill(variables)
        var_elim = self.reasoner.variable_elimination(factors, min_fill)
        stop = timeit.default_timer()

        print_experiment_results({
            "name": "ordering",
            "type": "min_fill",
            "bn_size": 31,
            "runtime": round(stop - start, 2)
        })


def print_experiment_results(results):
    for k, v in results.items():
        print(f"{k}: {v}")
    print()
