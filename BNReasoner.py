from typing import Union, List, Dict

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

    def is_d_separated(self, x: List[str], y: List[str], z: List[str]):
        paths = util.get_all_paths(self.bn, x, y)
        triplets = util.split_path_into_triplets(list(paths))

        for i, path in enumerate(triplets):
            is_path_blocked = util.is_path_blocked(self.bn, path, z)
            if not is_path_blocked:
                return False
        return True

    def is_independent(self, x: List[str], y: List[str], z: List[str]):
        return self.is_d_separated(x, y, z)

    def marginalize(self, factor: pd.DataFrame, x: List[str]):
        factor = factor.drop(x, axis=1)
        columns = factor.columns.values.tolist()[:-1]

        if len(columns) == 0:
            factor = factor.sum()
        else:
            factor = factor.groupby(columns).sum().reset_index()
        return factor

    def maxing_out(self, factor: pd.DataFrame, x: List[str]):
        factor = factor.drop(x, axis=1)
        columns = factor.columns.values.tolist()[:-1]

        if len(columns) == 0:
            factor = factor.max()
        else:
            factor = factor.groupby(columns).max().reset_index()
        return factor

    def factor_multiplication(self, factor_1, factor_2):
        # Setup factors and
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

    def compute_ordering_min_deg(self, x: List[str]):
        int_graph = self.bn.get_interaction_graph()
        ordering = []

        while len(x) > 0:
            node_to_delete = x[0]
            min_deg = util.get_degree_int_graph(int_graph, node_to_delete)

            for node in x:
                degree = util.get_degree_int_graph(int_graph, node)
                if degree < min_deg:
                    min_deg = degree
                    node_to_delete = node

            # print(node_to_delete)
            int_graph = util.del_var_int_graph(int_graph, node_to_delete)
            x.remove(node_to_delete)
            ordering.append(node_to_delete)

        return ordering

    def compute_ordering_min_fill(self, x: List[str]):
        int_graph = self.bn.get_interaction_graph()
        ordering = []

        while len(x) > 0:
            node_to_delete = x[0]
            min_fill = len(util.get_new_interactions(
                int_graph, node_to_delete))

            for node in x:
                fill = len(util.get_new_interactions(int_graph, node))
                if fill < min_fill:
                    min_fill = fill
                    node_to_delete = node

            # print(node_to_delete)
            int_graph = util.del_var_int_graph(int_graph, node_to_delete)
            x.remove(node_to_delete)
            ordering.append(node_to_delete)

        return ordering

    def draw_structure(self):
        self.bn.draw_structure()

    def two_f_multiplication(self, table_1, table_2):
        # Setup
        f1_vars = list(table_1.keys())
        f2_vars = list(table_2.keys())
        result_vars = list(set(f1_vars[:-1] + f2_vars[:-1]))
        column_names = result_vars[:]
        column_names.append('p')
        result_list = []
        # calculate p for all boolean_combinations
        bool_combinations = util.bool_combinator(len(result_vars))
        for combination in bool_combinations:
            instanciation = util.create_instantiation(combination, result_vars)
            instanciation_series = pd.Series(instanciation)
            # Get compatable rows per original factor
            p_table_1 = self.bn.get_compatible_instantiations_table(
                instanciation_series, table_1)['p'].values[0]
            p_table_2 = self.bn.get_compatible_instantiations_table(
                instanciation_series, table_2)['p'].values[0]
            multiplied_p = p_table_1 * p_table_2
            instanciation['p'] = multiplied_p
            result_list.append(instanciation)
        return pd.DataFrame(result_list, columns=column_names)

    def n_f_multiplication(self, factors):
        while factors:
            if len(factors) == 1:
                return factors[0]
            else:
                factors.append(self.two_f_multiplication(
                    factors.pop(), factors.pop()))

        return "Input was an empty list"

    def variable_elimination(self, factors, target_var):
        all_factors_list = [i for i in factors.values()]
        # Here should be the algorithm ordering the variables(now just getting all, -2)
        variable_order = self.compute_ordering_min_deg(target_var)
        # Elimination as defined in variable_order
        for var in variable_order:
            factors_to_remove = []
            all_factors_copy = list(all_factors_list)
            # split factors: var in f, ~var in f
            for i in range(0, len(all_factors_list)):
                current_factor = all_factors_copy[i]
                curr_f_vars = current_factor.columns.values.tolist()

                if var in curr_f_vars:
                    factors_to_remove.append(current_factor)
                    all_factors_list = [
                        x for x in all_factors_list if not x.equals(current_factor)]

            # Get factor after multiplying factors to remove
            if factors_to_remove:
                reduced_factor = self.n_f_multiplication(factors_to_remove)
                # Sum out current variable to elminate from reduced factor
                summed_factor = self.marginalize(reduced_factor, var)
                # Add factor to all_factors
                all_factors_list.append(summed_factor)
                # Get final factor
        final_factor = self.n_f_multiplication(all_factors_list)

        return final_factor

    def marginal_distribution(self, query_vars: List[str], evidence: Dict[str, bool]):
        factors = self.bn.get_all_cpts()
        for var_name, df in factors.items():
            factors[var_name] = self.bn.reduce_factor(pd.Series(evidence), df)

        ordering = list(set(self.bn.get_all_variables()) - set(query_vars))
        var_elim = pd.DataFrame(self.variable_elimination(factors, ordering))

        summed_out = self.marginalize(var_elim, query_vars).values[0]
        var_elim["p"] = var_elim["p"].div(summed_out).round(2)

        return var_elim
