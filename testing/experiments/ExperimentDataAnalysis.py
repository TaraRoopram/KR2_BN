import json
import unittest
import numpy as np
import os
import timeit
from typing import Union, List, TextIO

from BNReasoner import BNReasoner
from BayesNet import BayesNet

ROUND_NUM = 5


class ExperimentDataAnalysis(unittest.TestCase):
    def test_analysis_ordering_100(self):
        ordering_stats = []
        for file in os.listdir("./results"):
            if file.endswith("min_deg_100.json") or file.endswith("min_fill_100.json"):
                file_name = os.path.join("./results", file)
                stats = calculate_runtime_stats_from_file(file_name)
                ordering_stats.append(stats)

        ordering_stats = sorted(ordering_stats, key=lambda k: k["bn_size"])
        save_json_data(ordering_stats, "./stats/stats_ordering_100.json")

    def test_analysis_sum_out_100(self):
        ordering_stats = []
        for file in os.listdir("./results"):
            if file.endswith("naive_100.json") or file.endswith("var_elim_100.json"):
                file_name = os.path.join("./results", file)
                stats = calculate_runtime_stats_from_file(file_name)
                ordering_stats.append(stats)

        ordering_stats = sorted(ordering_stats, key=lambda k: k["bn_size"])
        save_json_data(ordering_stats, "./stats/stats_sum_out_100.json")


def load_json_data(file_path: Union[str, TextIO]):
    if isinstance(file_path, str):
        with open(file_path, "r") as file:
            return json.load(file)
    return json.load(file_path)


def save_json_data(data, file_path: Union[str, TextIO]):
    if isinstance(file_path, str):
        with open(file_path, "w+") as file:
            return json.dump(data, file, indent=3)
    return json.dump(data, file_path, indent=3)


def calculate_statistics(data):
    return {
        "mean": np.round(np.mean(data), ROUND_NUM),
        "std": np.round(np.std(data), ROUND_NUM),
        "max": np.round(np.max(data), ROUND_NUM),
        "min": np.round(np.min(data), ROUND_NUM),
        "range": np.round(np.max(data) - np.min(data), ROUND_NUM)
    }


def calculate_runtime_stats_from_file(file_path):
    data = load_json_data(file_path)
    data["runtime_stats"] = calculate_statistics(data["runtime"])
    del data["runtime"]
    return data
