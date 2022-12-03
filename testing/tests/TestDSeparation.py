import unittest

from BNReasoner import BNReasoner
from BayesNet import BayesNet
import BNReasonerUtil as util


class TestDSeparationL1(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../lecture_example.BIFXML")
        self.reasoner = BNReasoner(self.bn)


class TestDSeparationL2(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../lecture_example2.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_triplet_types(self):
        paths = util.get_all_paths(self.bn, "I", "O", [])
        triplets = util.split_path_into_triplets(list(paths))

        for i, path in enumerate(triplets):
            print(f"Path {i+1}")
            for triplet in path:
                x, y, z = triplet
                util.is_blocked(self.bn, x, y, z, [])
            print()


class TestDSeparationExample3(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../test_example_1.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_ex3_triplet_types_1(self):
        paths = util.get_all_paths(self.bn, "B", "C", [])
        triplets = util.split_path_into_triplets(list(paths))

        for i, path in enumerate(triplets):
            print(f"Path {i+1}")
            for triplet in path:
                x, y, z = triplet
                util.is_blocked(self.bn, x, y, z, ["A", "E"])
            print()
