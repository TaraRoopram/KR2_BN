import unittest

from BNReasoner import BNReasoner
from BayesNet import BayesNet
import BNReasonerUtil as util


@unittest.skip
class TestBNCommonExample1(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../bifxml/lecture_example.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_l1_get_all_paths_1(self):
        start = "Slippery Road?"
        end = "Sprinkler?"
        paths = util.get_all_paths(self.bn, start, end, [])
        self.assertEqual(len(paths), 2)
        self.assertEqual(paths[0], ["Slippery Road?", "Rain?", "Wet Grass?", "Sprinkler?"])
        self.assertEqual(paths[1], ["Slippery Road?", "Rain?", "Winter?", "Sprinkler?"])

    def test_l1_get_all_paths_2(self):
        start = "Slippery Road?"
        end = "Winter?"
        paths = util.get_all_paths(self.bn, start, end, [])
        self.assertEqual(len(paths), 2)
        self.assertEqual(paths[0], ["Slippery Road?", "Rain?", "Wet Grass?", "Sprinkler?", "Winter?"])
        self.assertEqual(paths[1], ["Slippery Road?", "Rain?", "Winter?"])

    def test_l1_get_descendants_1(self):
        variable = "Rain?"
        descendants = util.get_descendants(self.bn, variable, [])
        self.assertEqual(len(descendants), 2)
        self.assertEqual(descendants[0], "Wet Grass?")
        self.assertEqual(descendants[1], "Slippery Road?")

    def test_l1_get_descendants_2(self):
        variable = "Winter?"
        descendants = util.get_descendants(self.bn, variable, [])
        self.assertEqual(len(descendants), 4)
        self.assertEqual(descendants[0], "Sprinkler?")
        self.assertEqual(descendants[1], "Wet Grass?")
        self.assertEqual(descendants[2], "Rain?")
        self.assertEqual(descendants[3], "Slippery Road?")


@unittest.skip
class TestBNCommonExample2(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../bifxml/lecture_example2.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_l2_get_all_paths_1(self):
        start = "I"
        end = "O"
        paths = util.get_all_paths(self.bn, start, end, [])
        self.assertEqual(len(paths), 2)
        self.assertEqual(paths[0], ["I", "X", "O"])
        self.assertEqual(paths[1], ["I", "X", "J", "Y", "O"])

    def test_l2_get_all_paths_2(self):
        start = "I"
        end = "Y"
        paths = util.get_all_paths(self.bn, start, end, [])
        self.assertEqual(len(paths), 2)
        self.assertEqual(paths[0], ["I", "X", "O", "Y"])
        self.assertEqual(paths[1], ["I", "X", "J", "Y"])

    def test_l2_get_descendants_1(self):
        variable = "J"
        descendants = util.get_descendants(self.bn, variable, [])
        self.assertEqual(len(descendants), 3)
        self.assertEqual(descendants[0], "Y")
        self.assertEqual(descendants[1], "O")
        self.assertEqual(descendants[2], "X")

    def test_l2_get_descendants_2(self):
        variable = "I"
        descendants = util.get_descendants(self.bn, variable, [])
        self.assertEqual(len(descendants), 2)
        self.assertEqual(descendants[0], "X")
        self.assertEqual(descendants[1], "O")


@unittest.skip
class TestBNCommonExample3(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../bifxml/test_example_3.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_ex3_get_all_paths_1(self):
        start = "F"
        end = "C"
        paths = util.get_all_paths(self.bn, start, end, [])
        self.assertEqual(len(paths), 2)
        self.assertEqual(paths[0], ["F", "B", "D", "C"])
        self.assertEqual(paths[1], ["F", "B", "A", "C"])

    def test_ex3_get_all_paths_2(self):
        start = "F"
        end = "E"
        paths = util.get_all_paths(self.bn, start, end, [])
        self.assertEqual(len(paths), 2)
        self.assertEqual(paths[0], ["F", "B", "D", "E"])
        self.assertEqual(paths[1], ["F", "B", "A", "C", "D", "E"])
