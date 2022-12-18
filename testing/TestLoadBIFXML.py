import os
import unittest

from BNReasoner import BNReasoner
from BayesNet import BayesNet


class TestLoadBIFXML(unittest.TestCase):
    def setUp(self) -> None:
        self.bn = BayesNet()

    def test_load_bifxml_ex3(self):
        self.bn.load_from_bifxml(f"{os.path.dirname(os.path.abspath(__file__))}/bifxml/test_example_3.BIFXML")
        # self.bn.draw_structure()

    def test_load_bifxml_ex4(self):
        self.bn.load_from_bifxml(f"{os.path.dirname(os.path.abspath(__file__))}/bifxml/test_example_4.BIFXML")
        # self.bn.draw_structure()

    def test_load_bifxml_worksheet_2(self):
        self.bn.load_from_bifxml(f"{os.path.dirname(os.path.abspath(__file__))}/bifxml/test_example_worksheet_2.BIFXML")
        # self.bn.draw_structure()

    def test_load_bifxml_bin_tree_3(self):
        self.bn.load_from_bifxml(f"{os.path.dirname(os.path.abspath(__file__))}/../experiments/bifxml/bin_tree_3.BIFXML")
        self.assertTrue(is_child_of(self.bn, "A1", "Root"))
        self.assertTrue(is_child_of(self.bn, "A2", "Root"))

    def test_load_bifxml_bin_tree_7(self):
        self.bn.load_from_bifxml(f"{os.path.dirname(os.path.abspath(__file__))}/../experiments/bifxml/bin_tree_7.BIFXML")
        self.assertTrue(is_child_of(self.bn, "A1", "Root"))
        self.assertTrue(is_child_of(self.bn, "A2", "Root"))

        self.assertTrue(is_child_of(self.bn, "B1", "A1"))
        self.assertTrue(is_child_of(self.bn, "B2", "A1"))
        self.assertTrue(is_child_of(self.bn, "B3", "A2"))
        self.assertTrue(is_child_of(self.bn, "B4", "A2"))

    def test_load_bifxml_bin_tree_15(self):
        self.bn.load_from_bifxml(f"{os.path.dirname(os.path.abspath(__file__))}/../experiments/bifxml/bin_tree_15.BIFXML")
        self.assertTrue(is_child_of(self.bn, "A1", "Root"))
        self.assertTrue(is_child_of(self.bn, "A2", "Root"))

        self.assertTrue(is_child_of(self.bn, "B1", "A1"))
        self.assertTrue(is_child_of(self.bn, "B2", "A1"))
        self.assertTrue(is_child_of(self.bn, "B3", "A2"))
        self.assertTrue(is_child_of(self.bn, "B4", "A2"))

        self.assertTrue(is_child_of(self.bn, "C1", "B1"))
        self.assertTrue(is_child_of(self.bn, "C2", "B1"))
        self.assertTrue(is_child_of(self.bn, "C3", "B2"))
        self.assertTrue(is_child_of(self.bn, "C4", "B2"))
        self.assertTrue(is_child_of(self.bn, "C5", "B3"))
        self.assertTrue(is_child_of(self.bn, "C6", "B3"))
        self.assertTrue(is_child_of(self.bn, "C7", "B4"))
        self.assertTrue(is_child_of(self.bn, "C8", "B4"))

    def test_load_bifxml_bin_tree_31(self):
        self.bn.load_from_bifxml(f"{os.path.dirname(os.path.abspath(__file__))}/../experiments/bifxml/bin_tree_31.BIFXML")
        self.assertTrue(is_child_of(self.bn, "A1", "Root"))
        self.assertTrue(is_child_of(self.bn, "A2", "Root"))

        self.assertTrue(is_child_of(self.bn, "B1", "A1"))
        self.assertTrue(is_child_of(self.bn, "B2", "A1"))
        self.assertTrue(is_child_of(self.bn, "B3", "A2"))
        self.assertTrue(is_child_of(self.bn, "B4", "A2"))

        self.assertTrue(is_child_of(self.bn, "C1", "B1"))
        self.assertTrue(is_child_of(self.bn, "C2", "B1"))
        self.assertTrue(is_child_of(self.bn, "C3", "B2"))
        self.assertTrue(is_child_of(self.bn, "C4", "B2"))
        self.assertTrue(is_child_of(self.bn, "C5", "B3"))
        self.assertTrue(is_child_of(self.bn, "C6", "B3"))
        self.assertTrue(is_child_of(self.bn, "C7", "B4"))
        self.assertTrue(is_child_of(self.bn, "C8", "B4"))

        self.assertTrue(is_child_of(self.bn, "D1", "C1"))
        self.assertTrue(is_child_of(self.bn, "D2", "C1"))
        self.assertTrue(is_child_of(self.bn, "D3", "C2"))
        self.assertTrue(is_child_of(self.bn, "D4", "C2"))
        self.assertTrue(is_child_of(self.bn, "D5", "C3"))
        self.assertTrue(is_child_of(self.bn, "D6", "C3"))
        self.assertTrue(is_child_of(self.bn, "D7", "C4"))
        self.assertTrue(is_child_of(self.bn, "D8", "C4"))
        self.assertTrue(is_child_of(self.bn, "D9", "C5"))
        self.assertTrue(is_child_of(self.bn, "D10", "C5"))
        self.assertTrue(is_child_of(self.bn, "D11", "C6"))
        self.assertTrue(is_child_of(self.bn, "D12", "C6"))
        self.assertTrue(is_child_of(self.bn, "D13", "C7"))
        self.assertTrue(is_child_of(self.bn, "D14", "C7"))
        self.assertTrue(is_child_of(self.bn, "D15", "C8"))
        self.assertTrue(is_child_of(self.bn, "D16", "C8"))


def is_child_of(bn: BayesNet, node: str, parent: str):
    return node in bn.get_children(parent)
