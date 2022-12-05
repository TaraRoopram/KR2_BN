import unittest

from BNReasoner import BNReasoner
from BayesNet import BayesNet


class TestLoadBIFXML(unittest.TestCase):
    def setUp(self) -> None:
        self.bn = BayesNet()

    def test_load_bifxml_ex3(self):
        self.bn.load_from_bifxml("../test_example_3.BIFXML")
        # self.bn.draw_structure()

    def test_load_bifxml_ex4(self):
        self.bn.load_from_bifxml("../test_example_4.BIFXML")
        self.bn.draw_structure()
