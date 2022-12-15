import unittest
import networkx as nx
import pandas as pd
from matplotlib import pyplot as plt

from BNReasoner import BNReasoner
from BayesNet import BayesNet
import BNReasonerUtil as util


class TestFactorMultiplicationExample2(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../bifxml/lecture_example2.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_ex2_multiply_factors_empty(self):
        factor_1 = self.bn.get_cpt("I")
        factor_2 = self.bn.get_cpt("J")
        mult = self.reasoner.factor_multiplication(factor_1, factor_2).reset_index(drop=True)

        query = {"I": False, "J": False}
        self.assertEqual(query_cpt_p(mult, query), 0.5 * 0.5)

        query = {"I": False, "J": True}
        self.assertEqual(query_cpt_p(mult, query), 0.5 * 0.5)

        query = {"I": True, "J": False}
        self.assertEqual(query_cpt_p(mult, query), 0.5 * 0.5)

        query = {"I": True, "J": True}
        self.assertEqual(query_cpt_p(mult, query), 0.5 * 0.5)


class TestFactorMultiplicationExample3(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../bifxml/test_example_3.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_ex3_multiply_factors_small(self):
        factor_1 = self.bn.get_cpt("A")
        factor_2 = self.bn.get_cpt("B")
        mult = self.reasoner.factor_multiplication(factor_1, factor_2).reset_index(drop=True)

        query = {"A": False, "B": False}
        self.assertEqual(query_cpt_p(mult, query), 0.9 * 0.4)

        query = {"A": False, "B": True}
        self.assertEqual(query_cpt_p(mult, query), 0.4 * 0.1)

        query = {"A": True, "B": False}
        self.assertEqual(query_cpt_p(mult, query), 0.6 * 0.2)

        query = {"A": True, "B": True}
        self.assertEqual(query_cpt_p(mult, query), 0.6 * 0.8)

    def test_ex3_multiply_factors_large(self):
        factor_1 = self.bn.get_cpt("D")
        factor_2 = self.bn.get_cpt("F")
        mult = self.reasoner.factor_multiplication(factor_1, factor_2).reset_index(drop=True)

        query = {"C": False, "B": False, "D": False, "F": False}
        self.assertEqual(query_cpt_p(mult, query), 1 * 0.9)

        query = {"C": False, "B": False, "D": False, "F": True}
        self.assertEqual(query_cpt_p(mult, query), 1 * 0.1)

        query = {"C": False, "B": False, "D": True, "F": False}
        self.assertEqual(query_cpt_p(mult, query), 0.9 * 0)

        query = {"C": False, "B": False, "D": True, "F": True}
        self.assertEqual(query_cpt_p(mult, query), 0 * 0.1)

        query = {"C": False, "B": True, "D": False, "F": False}
        self.assertEqual(query_cpt_p(mult, query), 0.2 * 0.2)

        query = {"C": False, "B": True, "D": False, "F": True}
        self.assertEqual(query_cpt_p(mult, query), 0.2 * 0.8)

        query = {"C": False, "B": True, "D": True, "F": True}
        self.assertEqual(query_cpt_p(mult, query), 0.8 * 0.8)

        query = {"C": True, "B": False, "D": False, "F": False}
        self.assertEqual(query_cpt_p(mult, query), 0.1 * 0.9)

        query = {"C": True, "B": False, "D": False, "F": True}
        self.assertEqual(query_cpt_p(mult, query), 0.1 * 0.1)

        query = {"C": True, "B": False, "D": True, "F": False}
        self.assertEqual(query_cpt_p(mult, query), 0.9 * 0.9)

        query = {"C": True, "B": False, "D": True, "F": True}
        self.assertEqual(query_cpt_p(mult, query), 0.9 * 0.1)

        query = {"C": True, "B": True, "D": False, "F": False}
        self.assertEqual(query_cpt_p(mult, query), 0.05 * 0.2)

        query = {"C": True, "B": True, "D": False, "F": True}
        self.assertEqual(query_cpt_p(mult, query), 0.05 * 0.8)

        query = {"C": True, "B": True, "D": True, "F": False}
        self.assertEqual(query_cpt_p(mult, query), 0.95 * 0.2)

        query = {"C": True, "B": True, "D": True, "F": True}
        self.assertEqual(query_cpt_p(mult, query), 0.95 * 0.8)


def query_cpt(cpt, query_dict):
    query = True
    for var_name, query_val in query_dict.items():
        query &= (cpt[var_name] == query_val)
    return cpt[query]


def query_cpt_p(cpt, query_dict):
    return query_cpt(cpt, query_dict)["p"].iloc[0]
