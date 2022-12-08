import unittest
import networkx as nx
from matplotlib import pyplot as plt

from BNReasoner import BNReasoner
from BayesNet import BayesNet
import BNReasonerUtil as util

class TestFactorMulitplicationExample1(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../lecture_example.BIFXML")
        self.reasoner = BNReasoner(self.bn)

class TestFactorMulitplicationExample2(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../lecture_example2.BIFXML")
        self.reasoner = BNReasoner(self.bn)

class TestFactorMulitplicationExample3(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../test_example_3.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_ex3_multiply_factors(self):
        factor_1 = self.bn.get_cpt("A")
        factor_2 = self.bn.get_cpt("B")
        multiplied = self.reasoner.factor_multiplication(factor_1, factor_2)

        real_data = {
            "A": [False, False, True, True],
            "B": [False, True, False, True],
            "p": []
        }

        print(multiplied)


class TestFactorMulitplicationExample4(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../test_example_4.BIFXML")
        self.reasoner = BNReasoner(self.bn)

