import unittest
import networkx as nx
from matplotlib import pyplot as plt

from BNReasoner import BNReasoner
from BayesNet import BayesNet
import BNReasonerUtil as util


class TestOrderingExample1(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../lecture_example.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_ex3_number_of_new_interactions(self):
        var_to_delete = "Sprinkler?"
        util.get_number_of_new_interactions(self.bn, var_to_delete)
