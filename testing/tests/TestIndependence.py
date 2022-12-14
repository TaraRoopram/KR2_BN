import unittest

from BNReasoner import BNReasoner
from BayesNet import BayesNet


class TestIndependenceLectureExample1(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../test_example_4.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_lecture_example_1_indep_1(self):
        x = ["B"]
        y = ["C"]
        z = ["S"]

        indep = self.reasoner.is_independent(x, y, z)
        self.assertEqual(indep, True)

    def test_lecture_example_1_indep_2(self):
        x = ["X"]
        y = ["S"]
        z = ["C", "D"]

        indep = self.reasoner.is_independent(x, y, z)
        self.assertEqual(indep, False)

    def test_lecture_example_1_indep_3(self):
        x = ["X"]
        y = ["S"]
        z = ["C"]

        indep = self.reasoner.is_independent(x, y, z)
        self.assertEqual(indep, True)

    def test_lecture_example_1_indep_4(self):
        x = ["X", "S"]
        y = ["D"]
        z = ["B", "P"]

        indep = self.reasoner.is_independent(x, y, z)
        self.assertEqual(indep, True)

    def test_lecture_example_1_indep_5(self):
        x = ["A", "S"]
        y = ["D", "X"]
        z = ["B", "P"]

        indep = self.reasoner.is_independent(x, y, z)
        self.assertEqual(indep, True)

    def test_lecture_example_1_indep_6(self):
        x = ["T", "C"]
        y = ["B"]
        z = ["S", "X"]

        indep = self.reasoner.is_independent(x, y, z)
        self.assertEqual(indep, True)


class TestIndependenceLectureExample2(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../test_example_7.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_lecture_example_2_indep_1(self):
        x = ["C"]
        y = ["B", "E", "R"]
        z = ["A"]

        indep = self.reasoner.is_independent(x, y, z)
        self.assertEqual(indep, True)

    def test_lecture_example_2_indep_2(self):
        x = ["R"]
        y = ["A", "B", "C"]
        z = ["E"]

        indep = self.reasoner.is_independent(x, y, z)
        self.assertEqual(indep, True)

    def test_lecture_example_2_indep_3(self):
        x = ["A"]
        y = ["R"]
        z = ["B", "E"]

        indep = self.reasoner.is_independent(x, y, z)
        self.assertEqual(indep, True)

    def test_lecture_example_2_indep_4(self):
        x = ["B"]
        y = ["E", "R"]
        z = []

        indep = self.reasoner.is_independent(x, y, z)
        self.assertEqual(indep, True)

    def test_lecture_example_2_indep_5(self):
        x = ["E"]
        y = ["B"]
        z = []

        indep = self.reasoner.is_independent(x, y, z)
        self.assertEqual(indep, True)
