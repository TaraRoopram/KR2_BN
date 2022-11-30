from typing import Union, List
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
        """"
        Given a set of query variables Q and evidence e, node- and edge-prune the Bayesian network s.t. queries of the
        form P(Q|E) can still be correctly calculated. (3.5pts)
        """

        for e in evidence:
            e_children = bn.get_children(e)
            for e_child in e_children:
                bn.del_edge((e, e_child))

        leaf_nodes = [leaf_node for leaf_node in bn.get_all_variables() if len(bn.get_children(leaf_node)) == 0]
        for leaf_node in leaf_nodes:
            if leaf_node not in query_variables and leaf_node not in evidence:
                self.bn.del_var(leaf_node)

    def d_separation(self):
        pass

    def draw_structure(self):
        self.bn.draw_structure()



# edge: We can delete the outgoing edges of every node that is in the evidence 𝑒 without affecting the result of a
# query 𝑄. node: We can delete any leaf node that doesn’t appear in 𝑄 or 𝑒.


bn = BayesNet()
bn.load_from_bifxml("./testing/dog_problem.BIFXML")
# bn.draw_structure()

reasoner = BNReasoner(bn)
# reasoner.prune_network(query_variables=[], evidence=["Rain?"])
# reasoner.draw_structure()

util.get_all_paths(bn, "dog-out", "hear-bark")
