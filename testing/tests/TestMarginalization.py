import unittest

import pandas as pd
from pandas.testing import assert_frame_equal


from BNReasoner import BNReasoner
from BayesNet import BayesNet
import BNReasonerUtil as util


class TestMarginalizationExample1(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../lecture_example.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_ex1_marginalization_single_var_1(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = ["Rain?"]

        summed_out = self.reasoner.marginalize(factors, x)
        correct_summed_out = pd.DataFrame({
            "Sprinkler?": [False, False, True, True],
            "Wet Grass?": [False, True, False, True],
            "p": [1.2, 0.8, 0.10 + 0.05, 1.85]
        })

        self.assertTrue(correct_summed_out.equals(summed_out))

    def test_ex1_marginalization_single_var_2(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = ["Sprinkler?"]

        summed_out = self.reasoner.marginalize(factors, x)
        correct_summed_out = pd.DataFrame({
            "Rain?": [False, False, True, True],
            "Wet Grass?": [False, True, False, True],
            "p": [1.1, 0.9, 0.25, 1.75]
        })

        self.assertTrue(correct_summed_out.equals(summed_out))

    def test_ex1_marginalization_single_var_3(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = ["Wet Grass?"]

        summed_out = self.reasoner.marginalize(factors, x)
        correct_summed_out = pd.DataFrame({
            "Sprinkler?": [False, False, True, True],
            "Rain?": [False, True, False, True],
            "p": [1., 1., 1., 1.]
        })

        self.assertTrue(correct_summed_out.equals(summed_out))

    def test_ex1_marginalization_multiple_vars(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = ["Sprinkler?", "Rain?"]

        summed_out = self.reasoner.marginalize(factors, x)
        correct_summed_out = pd.DataFrame({
            "Wet Grass?": [False, True],
            "p": [1.35, 2.65]
        })

        self.assertTrue(correct_summed_out.equals(summed_out))

    def test_ex1_marginalization_all_vars(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = ["Sprinkler?", "Rain?", "Wet Grass?"]

        summed_out = self.reasoner.marginalize(factors, x)
        correct_summed_out = pd.Series({
            "p": 4.
        })

        self.assertTrue(summed_out.equals(correct_summed_out))

