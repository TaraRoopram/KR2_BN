import unittest

import pandas as pd

from BNReasoner import BNReasoner
from BayesNet import BayesNet
import BNReasonerUtil as util


class TestMarginalizationExample1(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../lecture_example.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_ex1_marginalization_1(self):
        x = "Rain?"
        factors = self.bn.get_cpt("Wet Grass?")

        print(f"{x}")
        print(f"{factors}")

        summed_out = self.reasoner.marginalize(factors, x)
        print(summed_out)

    def test_ex1_marginalization_2(self):
        x = "Sprinkler?"
        factors = self.bn.get_cpt("Wet Grass?")

        print(f"{x}")
        print(f"{factors}")

        summed_out = self.reasoner.marginalize(factors, x)
        print(summed_out)
