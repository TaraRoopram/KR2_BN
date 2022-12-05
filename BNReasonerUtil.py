from typing import List
import networkx as nx
import itertools

from BayesNet import BayesNet


def get_all_paths(bn: BayesNet, start: List[str], end: List[str]):
    undirected = nx.to_undirected(bn.structure)
    paths = []
    for s in start:
        for e in end:
            paths += list(nx.all_simple_paths(undirected, s, e))
    return paths


def get_parents(bn: BayesNet, _var: str):
    parents = []
    variables = bn.get_all_variables()

    for var in variables:
        if _var in bn.get_children(var):
            parents.append(var)

    return parents


def get_descendants(bn: BayesNet, _var: str, descendants: List[str]):
    children = bn.get_children(_var)
    if len(children) == 0:
        return descendants

    for child in children:
        if child not in descendants:
            descendants.append(child)
        get_descendants(bn, child, descendants)

    return descendants


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


def is_path_blocked(bn: BayesNet, path: List[str], givens: List[str] = []):
    for triplet in path:
        x, y, z = triplet
        if is_blocked(bn, x, y, z, givens):
            return True
    return False


def is_blocked(bn: BayesNet, x: str, y: str, z: str, givens: List[str] = []):
    triplet_type = get_path_triplet_type(bn, x, y, z)
    if y not in givens:
        if triplet_type == "sequence" or triplet_type == "fork":
            return False
        elif triplet_type == "collider":
            if any(desc in givens for desc in get_descendants(bn, y, [])):
                return False
            else:
                return True
    elif y in givens:
        if triplet_type == "collider":
            return False
        elif triplet_type == "sequence" or triplet_type == "fork":
            return True

    print("No decision")
    return None


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


def get_combinations(vars):
    combinations = []
    for t in itertools.product([True, False], repeat=len(vars)):
        combinations.append(dict(zip(vars, t)))
    return combinations



# def get_all_paths(bn: BayesNet, start: str, end: str, path: List[str]):
#     path = path + [start]
#
#     if start == end:
#         return [path]
#
#     if start not in bn.get_all_variables():
#         return []
#     paths = []
#
#     children = bn.get_children(start)
#     for node in children:
#         if node not in path:
#             newpaths = get_all_paths(bn, node, end, path)
#             for newpath in newpaths:
#                 paths.append(newpath)
#
#     parents = get_parents(bn, start)
#     for node in parents:
#         if node not in path:
#             newpaths = get_all_paths(bn, node, end, path)
#             for newpath in newpaths:
#                 paths.append(newpath)
#
#     return paths
