import unittest
import networkx as nx
import pandas as pd
from matplotlib import pyplot as plt

from BNReasoner import BNReasoner
from BayesNet import BayesNet
import BNReasonerUtil as util


class TestNetworkPruningExample5(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../bifxml/test_example_5.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_ex2_network_pruning_multiple_e(self):
        query_vars = ["D"]
        evidence = {"A": True, "C": False}
        self.reasoner.prune_network(query_vars, evidence)

        cpt_a = self.bn.get_cpt("A").round(2)
        correct_cpt_a = pd.DataFrame({
            "A": [False, True],
            "p": [0.4, 0.6]
        })

        cpt_b = self.bn.get_cpt("B").round(2)
        correct_cpt_b = pd.DataFrame({
            "B": [False, True],
            "p": [0.8, 0.2]
        })

        cpt_c = self.bn.get_cpt("C").round(2)
        correct_cpt_c = pd.DataFrame({
            "C": [False, True],
            "p": [0.2, 0.8]
        })

        cpt_d = self.bn.get_cpt("D").round(2)
        correct_cpt_d = pd.DataFrame({
            "B": [False, False, True, True],
            "D": [False, True, False, True],
            "p": [1., 0., 0.1, 0.9]
        })

        self.assertTrue(correct_cpt_a.equals(cpt_a))
        self.assertTrue(correct_cpt_b.equals(cpt_b))
        self.assertTrue(correct_cpt_c.equals(cpt_c))
        self.assertTrue(correct_cpt_d.equals(cpt_d))

        self.assertEqual(len(self.bn.get_children("A")), 0)
        self.assertEqual(len(self.bn.get_children("B")), 1)
        self.assertEqual(len(self.bn.get_children("C")), 0)
        self.assertEqual(len(self.bn.get_children("D")), 0)

    def test_ex2_network_pruning_multiple_Q(self):
        query_vars = ["E", "D"]
        evidence = {"B": True}
        self.reasoner.prune_network(query_vars, evidence)

        cpt_a = self.bn.get_cpt("A").round(2)
        correct_cpt_a = pd.DataFrame({
            "A": [False, True],
            "p": [0.4, 0.6]
        })

        cpt_b = self.bn.get_cpt("B").round(2)
        correct_cpt_b = pd.DataFrame({
            "A": [False, False, True, True],
            "B": [False, True, False, True],
            "p": [0.25, 0.75, 0.8, 0.2]
        })

        cpt_c = self.bn.get_cpt("C").round(2)
        correct_cpt_c = pd.DataFrame({
            "A": [False, False, True, True],
            "C": [False, True, False, True],
            "p": [0.9, 0.1, 0.2, 0.8]
        })

        cpt_d = self.bn.get_cpt("D").round(2)
        correct_cpt_d = pd.DataFrame({
            "C": [False, False, True, True],
            "D": [False, True, False, True],
            "p": [0.1, 0.9, 0.05, 0.95]
        })

        cpt_e = self.bn.get_cpt("E").round(2)
        correct_cpt_e = pd.DataFrame({
            "C": [False, False, True, True],
            "E": [False, True, False, True],
            "p": [1., 0., 0.3, 0.7]
        })

        self.assertTrue(correct_cpt_a.equals(cpt_a))
        self.assertTrue(correct_cpt_b.equals(cpt_b))
        self.assertTrue(correct_cpt_c.equals(cpt_c))
        self.assertTrue(correct_cpt_d.equals(cpt_d))
        self.assertTrue(correct_cpt_e.equals(cpt_e))

        self.assertEqual(len(self.bn.get_children("A")), 2)
        self.assertEqual(len(self.bn.get_children("B")), 0)
        self.assertEqual(len(self.bn.get_children("C")), 2)
        self.assertEqual(len(self.bn.get_children("D")), 0)
        self.assertEqual(len(self.bn.get_children("E")), 0)

    def test_ex2_network_pruning_multiple_Q_e(self):
        query_vars = ["A", "B"]
        evidence = {"C": True, "D": False}
        self.reasoner.prune_network(query_vars, evidence)

        cpt_a = self.bn.get_cpt("A").round(2)
        correct_cpt_a = pd.DataFrame({
            "A": [False, True],
            "p": [0.4, 0.6]
        })

        cpt_b = self.bn.get_cpt("B").round(2)
        correct_cpt_b = pd.DataFrame({
            "A": [False, False, True, True],
            "B": [False, True, False, True],
            "p": [0.25, 0.75, 0.8, 0.2]
        })

        cpt_c = self.bn.get_cpt("C").round(2)
        correct_cpt_c = pd.DataFrame({
            "A": [False, False, True, True],
            "C": [False, True, False, True],
            "p": [0.9, 0.1, 0.2, 0.8]
        })

        cpt_d = self.bn.get_cpt("D").round(2)
        correct_cpt_d = pd.DataFrame({
            "B": [False, False, True, True],
            "D": [False, True, False, True],
            "p": [0.2, 0.8, 0.05, 0.95]
        })

        self.assertTrue(correct_cpt_a.equals(cpt_a))
        self.assertTrue(correct_cpt_b.equals(cpt_b))
        self.assertTrue(correct_cpt_c.equals(cpt_c))
        self.assertTrue(correct_cpt_d.equals(cpt_d))

        self.assertEqual(len(self.bn.get_children("A")), 2)
        self.assertEqual(len(self.bn.get_children("B")), 1)
        self.assertEqual(len(self.bn.get_children("C")), 0)
        self.assertEqual(len(self.bn.get_children("D")), 0)

    def test_ex2_network_pruning_empty_Q(self):
        query_vars = []
        evidence = {"B": True}
        self.reasoner.prune_network(query_vars, evidence)

        cpt_a = self.bn.get_cpt("A").round(2)
        correct_cpt_a = pd.DataFrame({
            "A": [False, True],
            "p": [0.4, 0.6]
        })

        cpt_b = self.bn.get_cpt("B").round(2)
        correct_cpt_b = pd.DataFrame({
            "A": [False, False, True, True],
            "B": [False, True, False, True],
            "p": [0.25, 0.75, 0.8, 0.2]
        })

        self.assertTrue(correct_cpt_a.equals(cpt_a))
        self.assertTrue(correct_cpt_b.equals(cpt_b))

        self.assertEqual(len(self.bn.get_children("A")), 1)
        self.assertEqual(len(self.bn.get_children("B")), 0)
