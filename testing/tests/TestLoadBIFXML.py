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
        # self.bn.draw_structure()

    def test_load_bifxml_worksheet_2(self):
        self.bn.load_from_bifxml("../test_example_worksheet_2.BIFXML")
        cpts = self.bn.get_all_cpts()
        for cpt in cpts.values():
            print(cpt)
        # self.bn.draw_structure()
