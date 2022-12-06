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
        factors = self.bn.get_cpt("Wet Grass?")
        x = "Rain?"

        print(f"TO SUM OUT: {x}")
        print(f"{factors}")

        summed_out = self.reasoner.marginalize(factors, x)
        print(summed_out)

    def test_ex1_marginalization_2(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = "Sprinkler?"

        print(f"TO SUM OUT: {x}")
        print(f"{factors}")

        summed_out = self.reasoner.marginalize(factors, x)
        print(summed_out)

    def test_ex1_marginalization_3(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = "Wet Grass?"

        print(f"TO SUM OUT: {x}")
        print(f"{factors}")

        summed_out = self.reasoner.marginalize(factors, x)
        print(summed_out)

    def test_ex1_marginalization_4(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = ["Sprinkler?", "Rain?"]

        print(f"TO SUM OUT: {x}")
        print(f"{factors}")

        summed_out = self.reasoner.marginalize(factors, x)
        print(summed_out)

    def test_ex1_marginalization_5(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = ["Sprinkler?", "Rain?", "Wet Grass?"]

        print(f"TO SUM OUT: {x}")
        print(f"{factors}")

        summed_out = self.reasoner.marginalize(factors, x)
        print(summed_out)

