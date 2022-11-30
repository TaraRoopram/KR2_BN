import networkx as nx
from typing import List, Tuple

from BayesNet import BayesNet


def get_all_paths(bn: BayesNet, start: str, end: str):
    undirected = nx.to_undirected(bn.structure)
    paths = nx.all_simple_paths(undirected, source=start, target=end)
    return paths


def split_path_into_triplets(paths: List[str]):
    all_triplets = []
    for path in paths:
        triplets = []
        num_triplets = len(list(path)) - 2
        for i in range(num_triplets):
            triplet = path[i:(i + 3)]
            triplets.append(tuple(triplet))
        all_triplets.append(triplets)

    return all_triplets


def is_blocked(bn: BayesNet, x: str, y: Tuple[str, bool], z: str):
    triplet_type = get_path_triplet_type(bn, x, y[0], z)
    print(f"{x}, {y[0]}, {z} => {triplet_type}")


def get_path_triplet_type(bn: BayesNet, x: str, y: str, z: str):
    x_children = bn.get_children(x)
    y_children = bn.get_children(y)
    z_children = bn.get_children(z)

    if (y in x_children and z in y_children) or \
       (y in z_children and x in y_children):
        return "sequence"
    elif x in y_children and z in y_children:
        return "fork"
    elif y in x_children and y in z_children:
        return "collider"

    return None
