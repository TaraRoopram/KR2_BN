from typing import Union, List

import pandas as pd

from BayesNet import BayesNet
import BNReasonerUtil as util


class BNReasoner:
    def __init__(self, net: Union[str, BayesNet]):
        """
        :param net: either file path of the bayesian network in BIFXML format or BayesNet object
        """
        if type(net) == str:
            # constructs a BN object
            self.bn = BayesNet()
            # Loads the BN from an BIFXML file
            self.bn.load_from_bifxml(net)
        else:
            self.bn = net

    def prune_network(self, query_variables: List[str], evidence: List[str]):
        """
        Given a set of query variables Q and evidence e, node- and edge-prune the Bayesian network s.t. queries of the
        form P(Q|E) can still be correctly calculated. (3.5pts)
        """

        for e in evidence:
            e_children = self.bn.get_children(e)
            for e_child in e_children:
                self.bn.del_edge((e, e_child))

        leaf_nodes = [leaf_node for leaf_node in self.bn.get_all_variables() if len(
            self.bn.get_children(leaf_node)) == 0]
        for leaf_node in leaf_nodes:
            if leaf_node not in query_variables and leaf_node not in evidence:
                self.bn.del_var(leaf_node)

    def d_separation(self, x: List[str], y: List[str], z: List[str]):
        paths = util.get_all_paths(self.bn, x, y)
        triplets = util.split_path_into_triplets(list(paths))

        for i, path in enumerate(triplets):
            is_path_blocked = util.is_path_blocked(self.bn, path, z)
            if not is_path_blocked:
                return False

        return True

    def marginalize(self, factor: pd.DataFrame, x):
        factor = factor.drop(x, axis=1)
        factor = factor.groupby(factor.columns.values.tolist()[:-1]).sum()
        return factor

    def maxing_out(self, factor: pd.DataFrame, x):
        factor = factor.drop(x, axis=1)
        factor = factor.groupby(factor.columns.values.tolist()[:-1]).max()
        return factor

    def factor_multiplication(self, factor_1, factor_2):
        # Setup factors and
        print(factor_1)
        print(factor_2)
        f1_vars = list(factor_1.keys())
        f2_vars = list(factor_2.keys())

        result_vars = list(set(f1_vars[:-1] + f2_vars[:-1]))

        # init result dataframe
        column_names = result_vars[:]
        column_names.append('p')
        result_factor = pd.DataFrame([], column_names)
        result_list = []
        # calculate p for all boolean_combinations
        bool_combinations = util.bool_combinator(len(result_vars))
        for combination in bool_combinations:
            instanciation = util.create_instantiation(combination, result_vars)
            instanciation_series = pd.Series(instanciation)
            # Get compatable rows per original factor
            p_factor_1 = self.bn.get_compatible_instantiations_table(
                instanciation_series, factor_1)['p'].values[0]
            p_factor_2 = self.bn.get_compatible_instantiations_table(
                instanciation_series, factor_2)['p'].values[0]
            multiplied_p = p_factor_1 * p_factor_2
            instanciation['p'] = multiplied_p
            result_list.append(instanciation)

        columns = sorted(column_names)

        return pd.DataFrame(result_list, columns=column_names)

    def compute_ordering_min_deg(self):
        int_graph = self.bn.get_interaction_graph()
        nodes = list(int_graph.nodes)
        min_deg = util.get_degree_int_graph(int_graph, nodes[0])
        ordering = []

        while len(nodes) > 0:
            node_to_delete = nodes[0]
            for node in nodes:
                degree = util.get_degree_int_graph(int_graph, node)
                if degree < min_deg:
                    min_deg = degree
                    node_to_delete = node

            int_graph = util.del_var_int_graph(int_graph, node_to_delete)
            nodes = list(int_graph.nodes)
            ordering.append(node_to_delete)

        return ordering

    def compute_ordering_min_fill(self):
        int_graph = self.bn.get_interaction_graph()
        nodes = list(int_graph.nodes)
        min_fill = len(util.get_new_interactions(int_graph, nodes[0]))
        ordering = []

        while len(nodes) > 0:
            node_to_delete = nodes[0]
            for node in nodes:
                fill = len(util.get_new_interactions(int_graph, node))
                if fill < min_fill:
                    min_fill = fill
                    node_to_delete = node

            int_graph = util.del_var_int_graph(int_graph, node_to_delete)
            nodes = list(int_graph.nodes)
            ordering.append(node_to_delete)

        return ordering

    def draw_structure(self):
        self.bn.draw_structure()
