import os
import unittest

from BNReasoner import BNReasoner
from BayesNet import BayesNet


class TestMAPLectureExample2(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml(f"{os.path.dirname(os.path.abspath(__file__))}/bifxml/lecture_example2.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_ex2_map_1(self):
        query_vars = ["I", "J"]
        evidence = {"O": True}

        output_map = self.reasoner.MAP(query_vars, evidence)
        print(output_map)

    def test_ex2_map_2(self):
        query_vars = ["I", "J"]
        evidence = {"O": True}

        output_map = self.reasoner.MAP(query_vars, evidence)
        print(output_map)
