import unittest
import networkx as nx
import pandas as pd
from matplotlib import pyplot as plt

from BNReasoner import BNReasoner
from BayesNet import BayesNet
import BNReasonerUtil as util


class TestFactorMultiplicationExample1(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../lecture_example.BIFXML")
        self.reasoner = BNReasoner(self.bn)


class TestFactorMultiplicationExample2(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../lecture_example2.BIFXML")
        self.reasoner = BNReasoner(self.bn)


class TestFactorMultiplicationExample3(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../test_example_3.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_ex3_multiply_factors_1(self):
        factor_1 = self.bn.get_cpt("A")
        factor_2 = self.bn.get_cpt("B")
        mult = self.reasoner.factor_multiplication(factor_1, factor_2).reset_index(drop=True)

        query = {"A": False, "B": False}
        self.assertEqual(query_cpt_p(mult, query), 1 * 0.9)

    def test_ex3_multiply_factors_2(self):
        factor_1 = self.bn.get_cpt("D")
        factor_2 = self.bn.get_cpt("F")
        mult = self.reasoner.factor_multiplication(factor_1, factor_2).reset_index(drop=True)

        query = {"B": False, "C": False, "D": False, "F": False}
        self.assertEqual(query_cpt_p(mult, query), 1 * 0.9)

        query = {"B": False, "C": False, "D": True, "F": False}
        self.assertEqual(query_cpt_p(mult, query), 0 * 0.1)

        query = {"B": True, "C": False, "D": False, "F": False}
        self.assertEqual(query_cpt_p(mult, query), 0.2 * 0.2)

        query = {"B": True, "C": True, "D": True, "F": True}
        self.assertEqual(query_cpt_p(mult, query), 0.95 * 0.8)


class TestFactorMultiplicationExample4(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../test_example_4.BIFXML")
        self.reasoner = BNReasoner(self.bn)


def query_cpt(cpt, query_dict):
    query = True
    for var_name, query_val in query_dict.items():
        query &= (cpt[var_name] == query_val)
    return cpt[query]


def query_cpt_p(cpt, query_dict):
    return query_cpt(cpt, query_dict)["p"].iloc[0]
