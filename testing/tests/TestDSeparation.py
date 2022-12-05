import unittest

from BNReasoner import BNReasoner
from BayesNet import BayesNet
import BNReasonerUtil as util


class TestDSeparationExample1(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../lecture_example.BIFXML")
        self.reasoner = BNReasoner(self.bn)


class TestDSeparationExample2(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../lecture_example2.BIFXML")
        self.reasoner = BNReasoner(self.bn)


class TestDSeparationExample3(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../test_example_3.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_ex3_dsep_1(self):
        x = ["B"]
        y = ["C"]
        z = ["E"]

        dsep = self.reasoner.d_separation(x, y, z)
        self.assertEqual(dsep, False)

    def test_ex3_dsep_2(self):
        x = ["B"]
        y = ["C"]
        z = []

        dsep = self.reasoner.d_separation(x, y, z)
        self.assertEqual(dsep, False)


class TestDSeparationExample4(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../test_example_4.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_ex4_dsep_1(self):
        x = ["B"]
        y = ["C"]
        z = ["S"]

        dsep = self.reasoner.d_separation(x, y, z)
        self.assertEqual(dsep, True)

    def test_ex4_dsep_2(self):
        x = ["X"]
        y = ["S"]
        z = ["C", "D"]

        dsep = self.reasoner.d_separation(x, y, z)
        self.assertEqual(dsep, False)

    def test_ex4_dsep_3(self):
        x = ["X"]
        y = ["S"]
        z = ["C"]

        dsep = self.reasoner.d_separation(x, y, z)
        self.assertEqual(dsep, True)

    def test_ex4_dsep_4(self):
        x = ["X", "S"]
        y = ["D"]
        z = ["B", "P"]

        dsep = self.reasoner.d_separation(x, y, z)
        self.assertEqual(dsep, True)

    def test_ex4_dsep_5(self):
        x = ["A", "S"]
        y = ["D", "X"]
        z = ["B", "P"]

        dsep = self.reasoner.d_separation(x, y, z)
        self.assertEqual(dsep, True)

    def test_ex4_dsep_6(self):
        x = ["T", "C"]
        y = ["B"]
        z = ["S", "X"]

        dsep = self.reasoner.d_separation(x, y, z)
        self.assertEqual(dsep, True)
