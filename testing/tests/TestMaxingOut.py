import unittest
import pandas as pd


from BNReasoner import BNReasoner
from BayesNet import BayesNet


class TestMaxingOutExample1(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../lecture_example.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_ex1_maxingout_1(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = ["Rain?"]

        maxed_out = self.reasoner.maxing_out(factors, x).round(2)
        correct_maxed_out = pd.DataFrame({
            "Sprinkler?": [False, False, True, True],
            "Wet Grass?": [False, True, False, True],
            "p": [1.0, 0.8, 0.1, 0.95]
        })

        maxed_out_extended = self.reasoner.maxing_out(factors, x, extended=True)
        correct_maxed_out_extended = pd.DataFrame({
            "Sprinkler?": [False, False, True, True],
            "Wet Grass?": [False, True, False, True],
            "Rain?": [False, True, False, True],
            "p": [1.0, 0.8, 0.1, 0.95]
        })

        self.assertTrue(correct_maxed_out.equals(maxed_out))
        self.assertTrue(correct_maxed_out_extended.equals(maxed_out_extended))

    def test_ex1_maxingout_2(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = ["Sprinkler?"]

        maxed_out = self.reasoner.maxing_out(factors, x)
        correct_maxed_out = pd.DataFrame({
            "Rain?": [False, False, True, True],
            "Wet Grass?": [False, True, False, True],
            "p": [1.0, 0.9, 0.2, 0.95]
        })

        maxed_out_extended = self.reasoner.maxing_out(factors, x, extended=True)
        correct_maxed_out_extended = pd.DataFrame({
            "Rain?": [False, False, True, True],
            "Wet Grass?": [False, True, False, True],
            "Sprinkler?": [False, True, False, True],
            "p": [1.0, 0.9, 0.2, 0.95]
        })

        self.assertTrue(correct_maxed_out.equals(maxed_out))
        self.assertTrue(correct_maxed_out_extended.equals(maxed_out_extended))

    def test_ex1_maxingout_3(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = ["Wet Grass?"]

        maxed_out = self.reasoner.maxing_out(factors, x)
        correct_maxed_out = pd.DataFrame({
            "Sprinkler?": [False, False, True, True],
            "Rain?": [False, True, False, True],
            "p": [1., 0.8, 0.9, 0.95]
        })

        maxed_out_extended = self.reasoner.maxing_out(factors, x, extended=True)
        correct_maxed_out_extended = pd.DataFrame({
            "Sprinkler?": [False, False, True, True],
            "Rain?": [False, True, False, True],
            "Wet Grass?": [False, True, True, True],
            "p": [1., 0.8, 0.9, 0.95]
        })

        self.assertTrue(correct_maxed_out.equals(maxed_out))
        self.assertTrue(correct_maxed_out_extended.equals(maxed_out_extended))

    def test_ex1_maxingout_4(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = ["Sprinkler?", "Rain?"]

        print(factors)

        maxed_out = self.reasoner.maxing_out(factors, x)
        correct_maxed_out = pd.DataFrame({
            "Wet Grass?": [False, True],
            "p": [1, 0.95]
        })

        maxed_out_extended = self.reasoner.maxing_out(factors, x, extended=True)
        correct_maxed_out_extended = pd.DataFrame({
            "Wet Grass?": [False, True],
            "Sprinkler?": [False, True],
            "Rain?": [False, True],
            "p": [1, 0.95]
        })

        self.assertTrue(correct_maxed_out.equals(maxed_out))
        self.assertTrue(correct_maxed_out_extended.equals(maxed_out_extended))

    def test_ex1_maxingout_5(self):
        factors = self.bn.get_cpt("Wet Grass?")
        x = ["Sprinkler?", "Rain?", "Wet Grass?"]

        maxed_out = self.reasoner.maxing_out(factors, x)
        correct_maxed_out = pd.Series({
            "p": 1.
        })

        maxed_out_extended = self.reasoner.maxing_out(factors, x, extended=True)
        correct_maxed_out_extended = pd.Series({
            "Sprinkler?": False,
            "Rain?": False,
            "Wet Grass?": False,
            "p": 1.
        })

        self.assertTrue(maxed_out.equals(correct_maxed_out))
        self.assertTrue(correct_maxed_out_extended.equals(maxed_out_extended))
