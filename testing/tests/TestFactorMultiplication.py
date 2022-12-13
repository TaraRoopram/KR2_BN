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
        multiplied = self.reasoner.factor_multiplication(factor_1, factor_2)

        p = multiplied["p"].reset_index(drop=True).round(2)
        correct_p = pd.Series([0.04, 0.36, 0.48, 0.12], name="p").reset_index(drop=True)

        self.assertTrue(p.equals(correct_p))

    def test_ex3_multiply_factors_2(self):
        factor_1 = self.bn.get_cpt("D")
        factor_2 = self.bn.get_cpt("F")
        multiplied = self.reasoner.factor_multiplication(factor_1, factor_2).reset_index(drop=True)

        p = multiplied["p"].round(2)
        correct_p = pd.Series([0.04, 0.36, 0.48, 0.12], name="p").reset_index(drop=True)

        print(multiplied)

        self.assertTrue(p.equals(correct_p))


class TestFactorMultiplicationExample4(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../test_example_4.BIFXML")
        self.reasoner = BNReasoner(self.bn)
