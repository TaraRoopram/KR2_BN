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

    def test_lecture_example_marg_dist_1(self):
        query_vars = ["C"]
        evidence = {"A": True}

        marg_dist = self.reasoner.marginal_distribution(query_vars, evidence).round(2)
        correct_marg_dist = pd.DataFrame({
            "C": [False, True],
            "p": [0.68, 0.32]
        })

        self.assertTrue(marg_dist.equals(correct_marg_dist))


class TestMarginalDistributionWorksheet2(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../test_example_worksheet_2.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_worksheet_example_marg_dist_1(self):
        query_vars = ["T1"]
        evidence = {"S": False}

        marg_dist = self.reasoner.marginal_distribution(query_vars, evidence).round(2)
        correct_marg_dist = pd.DataFrame({
            "T1": [False, True],
            "p": [0.23, 0.77]
        })

        self.assertTrue(marg_dist.equals(correct_marg_dist))
