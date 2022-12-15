import unittest

from BNReasoner import BNReasoner
from BayesNet import BayesNet
import BNReasonerUtil as util


class TestDSeparationExample3(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../bifxml/test_example_3.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_ex3_dsep_1(self):
        x = ["B"]
        y = ["C"]
        z = ["E"]

        dsep = self.reasoner.is_d_separated(x, y, z)
        self.assertEqual(dsep, False)

    def test_ex3_dsep_2(self):
        x = ["B"]
        y = ["C"]
        z = []

        dsep = self.reasoner.is_d_separated(x, y, z)
        self.assertEqual(dsep, False)


class TestDSeparationLectureExample(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../bifxml/test_example_4.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_lecture_example_dsep_1(self):
        x = ["B"]
        y = ["C"]
        z = ["S"]

        dsep = self.reasoner.is_d_separated(x, y, z)
        self.assertEqual(dsep, True)

    def test_lecture_example_dsep_2(self):
        x = ["X"]
        y = ["S"]
        z = ["C", "D"]

        dsep = self.reasoner.is_d_separated(x, y, z)
        self.assertEqual(dsep, False)

    def test_lecture_example_dsep_3(self):
        x = ["X"]
        y = ["S"]
        z = ["C"]

        dsep = self.reasoner.is_d_separated(x, y, z)
        self.assertEqual(dsep, True)

    def test_lecture_example_dsep_4(self):
        x = ["X", "S"]
        y = ["D"]
        z = ["B", "P"]

        dsep = self.reasoner.is_d_separated(x, y, z)
        self.assertEqual(dsep, True)

    def test_lecture_example_dsep_5(self):
        x = ["A", "S"]
        y = ["D", "X"]
        z = ["B", "P"]

        dsep = self.reasoner.is_d_separated(x, y, z)
        self.assertEqual(dsep, True)

    def test_lecture_example_dsep_6(self):
        x = ["T", "C"]
        y = ["B"]
        z = ["S", "X"]

        dsep = self.reasoner.is_d_separated(x, y, z)
        self.assertEqual(dsep, True)
