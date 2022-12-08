import unittest

import pandas as pd

from BNReasoner import BNReasoner
from BayesNet import BayesNet
import BNReasonerUtil as util


class TestMaxingOutExample1(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../lecture_example.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_ex1_maxingout_1(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = "Rain?"

        print(f"TO MAX OUT: {x}")
        print(f"{factors}")

        maxed_out = self.reasoner.maxing_out(factors, x)
        print(maxed_out)

    def test_ex1_maxingout_2(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = "Sprinkler?"

        print(f"TO MAX OUT: {x}")
        print(f"{factors}")

        maxed_out = self.reasoner.maxing_out(factors, x)
        print(maxed_out)

    def test_ex1_maxingout_3(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = "Wet Grass?"

        print(f"TO MAX OUT: {x}")
        print(f"{factors}")

        maxed_out = self.reasoner.maxing_out(factors, x)
        print(maxed_out)

    def test_ex1_maxingout_4(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = ["Sprinkler?", "Rain?"]

        print(f"TO MAX OUT: {x}")
        print(f"{factors}")

        maxed_out = self.reasoner.maxing_out(factors, x)
        print(maxed_out)

    def test_ex1_maxingout_5(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = ["Sprinkler?", "Rain?", "Wet Grass?"]

        print(f"TO MAX OUT: {x}")
        print(f"{factors}")

        maxed_out = self.reasoner.maxing_out(factors, x)
        print(maxed_out)

