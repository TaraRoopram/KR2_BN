import unittest

import pandas as pd
from pandas.testing import assert_frame_equal


from BNReasoner import BNReasoner
from BayesNet import BayesNet
import BNReasonerUtil as util


class TestMarginalizationExample1(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn_2 = BayesNet()
        self.bn.load_from_bifxml("../lecture_example.BIFXML")
        self.bn2.load_from_bifxml("testing/test_example_6.BIFXML")
        self.reasoner = BNReasoner(self.bn)
        self.reasoner_2 = BNReasoner(self.bn_2)

    def test_ex1_marginalization_1(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = ["Rain?"]

        correct_summed_out = pd.DataFrame({
            "Sprinkler?": [False, False, True, True],
            "Wet Grass?": [False, True, False, True],
            "p": [1.2, 0.8, 0.10 + 0.05, 1.85]
        })

        summed_out = self.reasoner.variable_elimination(factors, x)
        self.assertTrue(correct_summed_out.equals(summed_out))

    def test_ex1_marginalization_2(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = ["Sprinkler?"]

        correct_summed_out = pd.DataFrame({
            "Rain?": [False, False, True, True],
            "Wet Grass?": [False, True, False, True],
            "p": [1.1, 0.9, 0.25, 1.75]
        })

        summed_out = self.reasoner.variable_elimination(factors, x)
        self.assertTrue(correct_summed_out.equals(summed_out))

    def test_ex1_marginalization_3(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = ["Wet Grass?"]

        correct_summed_out = pd.DataFrame({
            "Sprinkler?": [False, False, True, True],
            "Rain?": [False, True, False, True],
            "p": [1., 1., 1., 1.]
        })

        summed_out = self.reasoner.variable_elimination(factors, x)
        self.assertTrue(correct_summed_out.equals(summed_out))

    def test_ex1_variable_elimination_4(self):
        x = ["A", "B"]

        correct_variable_elminated = pd.DataFrame({
            "C": [True, False],
            "p": [0.376, 0.624]
        })

        variable_elminated = self.reasoner_2.variable_elimination(x)
        self.assertTrue(correct_variable_elminated.equals(variable_elminated))

    def test_ex1_variable_elimination_5(self):
        x = ["A"]

        correct_variable_elminated = pd.DataFrame({
            "B": [True, True, False, False],
            "C": [True, False, True, False],
            "p": [0.186, 0.434, 0.190, 0.190]
        })

        variable_elminated = self.reasoner_2.variable_elimination(x)
        self.assertTrue(correct_variable_elminated.equals(variable_elminated))
