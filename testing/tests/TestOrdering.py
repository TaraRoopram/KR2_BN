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

    def test_ex1_del_var_int_graph_1(self):
        var_to_delete = "Rain?"
        int_graph = self.bn.get_interaction_graph()
        new_edges = util.get_new_interactions(int_graph, var_to_delete)

        self.assertEqual(len(new_edges), 4)
        edge_1 = ("Winter?", "Wet Grass?")
        self.assertTrue(is_tuple_in_list(edge_1, new_edges))
        edge_2 = ("Winter?", "Slippery Road?")
        self.assertTrue(is_tuple_in_list(edge_2, new_edges))
        edge_3 = ("Sprinkler?", "Slippery Road?")
        self.assertTrue(is_tuple_in_list(edge_3, new_edges))
        edge_4 = ("Wet Grass?", "Slippery Road?")
        self.assertTrue(is_tuple_in_list(edge_4, new_edges))

        new_int_graph = util.del_var_int_graph(int_graph, var_to_delete)
        self.assertTrue(var_to_delete not in new_int_graph.nodes)
        self.assertTrue(are_edges_in_undirected_graph(new_int_graph, new_edges))

    def test_ex1_del_var_int_graph_2(self):
        var_to_delete = "Sprinkler?"
        int_graph = self.bn.get_interaction_graph()
        new_edges = util.get_new_interactions(int_graph, var_to_delete)

        self.assertEqual(len(new_edges), 1)
        edge_1 = ("Winter?", "Wet Grass?")
        self.assertTrue(is_tuple_in_list(edge_1, new_edges))

        new_int_graph = util.del_var_int_graph(int_graph, var_to_delete)
        self.assertTrue(var_to_delete not in new_int_graph.nodes)
        self.assertTrue(are_edges_in_undirected_graph(new_int_graph, new_edges))

    def test_ex1_del_var_int_graph_3(self):
        var_to_delete = "Winter?"
        int_graph = self.bn.get_interaction_graph()
        new_edges = util.get_new_interactions(int_graph, var_to_delete)

        self.assertEqual(len(new_edges), 0)

        new_int_graph = util.del_var_int_graph(int_graph, var_to_delete)
        self.assertTrue(var_to_delete not in new_int_graph.nodes)
        self.assertTrue(are_edges_in_undirected_graph(new_int_graph, new_edges))

    def test_ex1_min_deg_ordering_1(self):
        x = ["Sprinkler?", "Slippery Road?", "Winter?"]
        ordering = self.reasoner.compute_ordering_min_deg(x)
        correct_order = ["Slippery Road?", "Winter?", "Sprinkler?"]
        self.assertEqual(correct_order, ordering)

    def test_ex1_min_deg_ordering_2(self):
        x = ["Sprinkler?", "Rain?", "Slippery Road?", "Winter?"]
        ordering = self.reasoner.compute_ordering_min_deg(x)
        correct_order = ["Slippery Road?", "Winter?", "Sprinkler?", "Rain?"]
        self.assertEqual(correct_order, ordering)

    def test_ex1_min_fill_ordering_1(self):
        x = ["Sprinkler?", "Slippery Road?", "Winter?"]
        ordering = self.reasoner.compute_ordering_min_fill(x)
        correct_order = ["Slippery Road?", "Winter?", "Sprinkler?"]
        self.assertEqual(ordering, correct_order)

    def test_ex1_min_fill_ordering_2(self):
        x = ["Sprinkler?", "Rain?", "Slippery Road?", "Winter?"]
        ordering = self.reasoner.compute_ordering_min_fill(x)
        correct_order = ["Slippery Road?", "Winter?", "Sprinkler?", "Rain?"]
        self.assertEqual(ordering, correct_order)


class TestOrderingExample2(unittest.TestCase):
    def setUp(self):
        self.bn = BayesNet()
        self.bn.load_from_bifxml("../lecture_example2.BIFXML")
        self.reasoner = BNReasoner(self.bn)

    def test_ex2_del_var_int_graph_1(self):
        var_to_delete = "X"
        int_graph = self.bn.get_interaction_graph()
        new_edges = util.get_new_interactions(int_graph, var_to_delete)

        self.assertEqual(len(new_edges), 3)
        edge_1 = ("I", "O")
        self.assertTrue(is_tuple_in_list(edge_1, new_edges))
        edge_2 = ("I", "Y")
        self.assertTrue(is_tuple_in_list(edge_2, new_edges))
        edge_3 = ("J", "O")
        self.assertTrue(is_tuple_in_list(edge_3, new_edges))

        new_int_graph = util.del_var_int_graph(int_graph, var_to_delete)
        self.assertTrue(var_to_delete not in new_int_graph.nodes)
        self.assertTrue(are_edges_in_undirected_graph(new_int_graph, new_edges))

    def test_ex2_del_var_int_graph_2(self):
        var_to_delete = "J"
        int_graph = self.bn.get_interaction_graph()
        new_edges = util.get_new_interactions(int_graph, var_to_delete)

        self.assertEqual(len(new_edges), 1)
        edge_1 = ("I", "Y")
        self.assertTrue(is_tuple_in_list(edge_1, new_edges))

        new_int_graph = util.del_var_int_graph(int_graph, var_to_delete)
        self.assertTrue(var_to_delete not in new_int_graph.nodes)
        self.assertTrue(are_edges_in_undirected_graph(new_int_graph, new_edges))

    def test_ex2_del_var_int_graph_3(self):
        var_to_delete = "O"
        int_graph = self.bn.get_interaction_graph()
        new_edges = util.get_new_interactions(int_graph, var_to_delete)

        self.assertEqual(len(new_edges), 0)

        new_int_graph = util.del_var_int_graph(int_graph, var_to_delete)
        self.assertTrue(var_to_delete not in new_int_graph.nodes)
        self.assertTrue(are_edges_in_undirected_graph(new_int_graph, new_edges))

    def test_ex2_min_deg_ordering_1(self):
        x = ["J", "I"]
        ordering = self.reasoner.compute_ordering_min_deg(x)
        correct_order = ["I", "J"]
        self.assertEqual(ordering, correct_order)

    def test_ex2_min_deg_ordering_2(self):
        x = ["J", "X", "Y"]
        ordering = self.reasoner.compute_ordering_min_deg(x)
        correct_order = ["J", "X", "Y"]
        self.assertEqual(ordering, correct_order)

    def test_ex2_min_fill_ordering_1(self):
        x = ["J", "X", "Y"]
        ordering = self.reasoner.compute_ordering_min_fill(x)
        correct_order = ["J", "X", "Y"]
        self.assertEqual(ordering, correct_order)


def is_tuple_in_list(_tuple, _list):
    return _tuple in _list or tuple(reversed(_tuple)) in _list


def are_edges_in_undirected_graph(graph, edges):
    for edge in edges:
        if not ((edge[0], edge[1]) in graph.edges or (edge[1], edge[0]) in graph.edges):
            return False
    return True
