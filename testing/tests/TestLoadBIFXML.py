import unittest

from BNReasoner import BNReasoner
from BayesNet import BayesNet


class TestLoadBIFXML(unittest.TestCase):
    def setUp(self) -> None:
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../test_example_1.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_load_bifxml_1(self):
        self.bn.draw_structure()
