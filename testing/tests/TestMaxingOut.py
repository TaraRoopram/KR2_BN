import unittest

import pandas as pd
from pandas.testing import assert_frame_equal


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
        x = ["Rain?"]

        correct_maxed_out = pd.DataFrame({
            "Sprinkler?": [False, False, True, True],
            "Wet Grass?": [False, True, False, True],
            "p": [1.2, 0.8, 0.10 + 0.05, 1.85]
        })

        maxed_out = self.reasoner.maxing_out(factors, x)
        self.assertTrue(correct_maxed_out.equals(maxed_out))

    def test_ex1_maxingout_2(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = ["Sprinkler?"]

        correct_maxed_out = pd.DataFrame({
            "Rain?": [False, False, True, True],
            "Wet Grass?": [False, True, False, True],
            "p": [1.1, 0.9, 0.25, 1.75]
        })

        maxed_out = self.reasoner.maxing_out(factors, x)
        self.assertTrue(correct_maxed_out.equals(maxed_out))

    def test_ex1_maxingout_3(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = ["Wet Grass?"]

        correct_maxed_out = pd.DataFrame({
            "Sprinkler?": [False, False, True, True],
            "Rain?": [False, True, False, True],
            "p": [1., 1., 1., 1.]
        })

        maxed_out = self.reasoner.maxing_out(factors, x)
        self.assertTrue(correct_maxed_out.equals(maxed_out))

    def test_ex1_maxingout_4(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = ["Sprinkler?", "Rain?"]

        correct_maxed_out = pd.DataFrame({
            "Wet Grass?": [False, True],
            "p": [1.35, 2.65]
        })

        maxed_out = self.reasoner.maxing_out(factors, x)
        self.assertTrue(correct_maxed_out.equals(maxed_out))

    def test_ex1_maxingout_5(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = ["Sprinkler?", "Rain?", "Wet Grass?"]

        correct_maxed_out = pd.Series({
            "p": 4.
        })

        maxed_out = self.reasoner.maxing_out(factors, x)
        self.assertTrue(maxed_out.equals(correct_maxed_out))

