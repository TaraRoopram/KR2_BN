import networkx as nx

from BayesNet import BayesNet


def get_all_paths(bn: BayesNet, start: str, end: str):
    paths = nx.all_simple_paths(bn.structure, source=start, target=end)
    print(list(paths))

