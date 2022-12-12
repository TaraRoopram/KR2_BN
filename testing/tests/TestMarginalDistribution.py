import unittest

import pandas as pd

from BNReasoner import BNReasoner
from BayesNet import BayesNet
import BNReasonerUtil as util


class TestMarginalDistributionExample6(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../test_example_6.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_ex1_reduce_factors_1(self):
        query_vars = ["C"]
        evidence = {"A": True}
        marg_dist = self.reasoner.marginal_distribution(query_vars, evidence)
        print(marg_dist)


class TestMarginalDistributionWorksheet2(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../test_example_worksheet_2.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_ex1_reduce_factors_1(self):
        query_vars = ["T1"]
        evidence = {"S": False}
        marg_dist = self.reasoner.marginal_distribution(query_vars, evidence)
        print(marg_dist)
