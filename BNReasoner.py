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

    def draw_structure(self):
        self.bn.draw_structure()

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
            print(instanciation)
            print(p_factor_1)
            print(p_factor_2)
            multiplied_p = p_factor_1 * p_factor_2
            print(multiplied_p)
            print("---------")
            instanciation['p'] = multiplied_p
            result_list.append(instanciation)
            print(instanciation)
            # Append results as row to result_factor
        print(result_list)
        columns = sorted(column_names)
        # print(columns)

        # data = {
        #     "C": [True, False, ...],
        #     "D": [True, False],
        #     "p": [0, 0.1]
        # }

        return pd.DataFrame(result_list, columns=column_names)


