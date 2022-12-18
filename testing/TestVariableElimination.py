import os
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from BNReasoner import BNReasoner
from BayesNet import BayesNet
import BNReasonerUtil as util


class TestMarginalizationExample1(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml(f"{os.path.dirname(os.path.abspath(__file__))}/bifxml/lecture_example.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_ex1_var_elim_single_var_1(self):
        factor_name = "Wet Grass?"
        factors = {factor_name: self.bn.get_cpt(factor_name)}
        x = ["Rain?"]

        var_elim = self.reasoner.variable_elimination(factors, x)
        correct_var_elim = pd.DataFrame({
            "Sprinkler?": [False, False, True, True],
            "Wet Grass?": [False, True, False, True],
            "p": [1.2, 0.8, 0.10 + 0.05, 1.85]
        })

        self.assertTrue(correct_var_elim.equals(var_elim))

    def test_ex1_var_elim_single_var_2(self):
        factor_name = "Wet Grass?"
        factors = {factor_name: self.bn.get_cpt(factor_name)}
        x = ["Sprinkler?"]

        var_elim = self.reasoner.variable_elimination(factors, x)
        correct_var_elim = pd.DataFrame({
            "Rain?": [False, False, True, True],
            "Wet Grass?": [False, True, False, True],
            "p": [1.1, 0.9, 0.25, 1.75]
        })

        self.assertTrue(correct_var_elim.equals(var_elim))

    def test_ex1_var_elim_single_var_3(self):
        factor_name = "Wet Grass?"
        factors = {factor_name: self.bn.get_cpt(factor_name)}
        x = ["Wet Grass?"]

        var_elim = self.reasoner.variable_elimination(factors, x)
        correct_var_elim = pd.DataFrame({
            "Sprinkler?": [False, False, True, True],
            "Rain?": [False, True, False, True],
            "p": [1., 1., 1., 1.]
        })

        self.assertTrue(correct_var_elim.equals(var_elim))

    def test_ex1_var_elim_multiple_vars(self):
        factor_name = "Wet Grass?"
        factors = {factor_name: self.bn.get_cpt(factor_name)}
        x = ["Sprinkler?", "Rain?"]

        var_elim = self.reasoner.variable_elimination(factors, x)
        correct_var_elim = pd.DataFrame({
            "Wet Grass?": [False, True],
            "p": [1.35, 2.65]
        })

        self.assertTrue(correct_var_elim.equals(var_elim))

    def test_ex1_var_elim_all_vars(self):
        factor_name = "Wet Grass?"
        factors = {factor_name: self.bn.get_cpt(factor_name)}
        x = ["Sprinkler?", "Rain?", "Wet Grass?"]

        var_elim = self.reasoner.variable_elimination(factors, x)
        correct_var_elim = pd.Series({
            "p": 4.
        })

        self.assertTrue(var_elim.equals(correct_var_elim))

