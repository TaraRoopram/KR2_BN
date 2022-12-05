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

        leaf_nodes = [leaf_node for leaf_node in self.bn.get_all_variables() if len(self.bn.get_children(leaf_node)) == 0]
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

    def marginalize(self, factor: pd.DataFrame, x: str):
        factor = factor.drop(x, axis=1)
        factor = factor.groupby(factor.columns.values.tolist()[:-1]).sum()
        return factor

    def draw_structure(self):
        self.bn.draw_structure()
