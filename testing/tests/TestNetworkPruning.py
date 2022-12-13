import unittest
import networkx as nx
from matplotlib import pyplot as plt

from BNReasoner import BNReasoner
from BayesNet import BayesNet
import BNReasonerUtil as util


class TestNetworkPruningExample5(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../test_example_5.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_ex2_network_pruning_1(self):
        query_vars = ["D"]
        evidence = {"A": True, "C": False}
        self.reasoner.prune_network(query_vars, evidence)

        for cpt in self.bn.get_all_cpts().values():
            print(cpt)

    def test_ex2_network_pruning_2(self):
        query_vars = ["E", "D"]
        evidence = {"C": False}
        self.reasoner.prune_network(query_vars, evidence)

        for cpt in self.bn.get_all_cpts().values():
            print(cpt)
