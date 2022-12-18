import os
import json
import unittest
import matplotlib.pyplot as plt
from typing import Union, TextIO, Tuple
import numpy as np

ROUND_NUM = 5

SMALL_SIZE = 12
MEDIUM_SIZE = 14
BIGGER_SIZE = 18

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=BIGGER_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title


class ExperimentDataAnalysis(unittest.TestCase):
    def test_boxplot_runtime_ordering_100(self):
        min_deg_runtime_data, min_fill_runtime_data = get_runtime_data_split(("min_deg_100.json", "min_fill_100.json"))

        ticks = ["3", "7", "15", "31"]
        colors = [["#00539CFF", "#00539C77"], ["#3A6B35FF", "#3A6B3577"]]
        min_deg_bp = plt.boxplot(min_deg_runtime_data, positions=np.array(range(len(min_deg_runtime_data))) * 2.0 - 0.4,
                                 sym='', widths=0.6)
        min_fill_bp = plt.boxplot(min_fill_runtime_data,
                                  positions=np.array(range(len(min_fill_runtime_data))) * 2.0 + 0.4,
                                  sym='', widths=0.6)

        set_boxplot_colors(min_deg_bp,
                           boxes=colors[0][1], whiskers=colors[0][0], caps=colors[0][0], medians=colors[0][0])
        set_boxplot_colors(min_fill_bp,
                           boxes=colors[1][1], whiskers=colors[1][0], caps=colors[1][0], medians=colors[1][0])

        plt.plot([], c=colors[0][0], label='Min-deg.')
        plt.plot([], c=colors[1][0], label='Min-fill')
        plt.legend()

        plt.xticks(range(0, len(ticks) * 2, 2), ticks)
        plt.gca().yaxis.grid(True)

        plt.title("Boxplots showing the runtime of each ordering \n heuristic for "
                  "binary tree shaped BNs of varying size")
        plt.xlabel("Number of nodes in the BN")
        plt.ylabel("Runtime (s)")
        plt.show()

    def test_boxplot_runtime_sum_out_100(self):
        naive_runtime_data, var_elim_runtime_data = get_runtime_data_split(("naive_100.json", "var_elim_100.json"))

        ticks = ["3", "7", "15", "31"]
        colors = [["#00539CFF", "#00539C77"], ["#3A6B35FF", "#3A6B3577"]]
        naive_bp = plt.boxplot(naive_runtime_data, positions=np.array(range(len(naive_runtime_data))) * 2.0 - 0.4,
                               sym='', widths=0.6, patch_artist=True)
        var_elim_bp = plt.boxplot(var_elim_runtime_data,
                                  positions=np.array(range(len(var_elim_runtime_data))) * 2.0 + 0.4,
                                  sym='', widths=0.6, patch_artist=True)

        set_boxplot_colors(naive_bp,
                           boxes=colors[0][1], whiskers=colors[0][0], caps=colors[0][0], medians=colors[0][0])
        set_boxplot_colors(var_elim_bp,
                           boxes=colors[1][1], whiskers=colors[1][0], caps=colors[1][0], medians=colors[1][0])

        plt.plot([], c=colors[0][0], label='Naive')
        plt.plot([], c=colors[1][0], label='Var. elim.')
        plt.legend()

        plt.xticks(range(0, len(ticks) * 2, 2), ticks)
        plt.gca().yaxis.grid(True)

        plt.title("Boxplots showing the runtime of each summing out method \n for "
                  "binary tree shaped BNs of varying size")
        plt.xlabel("Number of nodes in the BN")
        plt.ylabel("Runtime (s)")
        plt.show()

    def test_bar_plot_ordering_100(self):
        min_deg_mean, min_fill_mean = get_mean_runtime_data_split("./stats/stats_ordering_100.json",
                                                                  "min_deg", "min_fill")
        labels = ["3", "7", "15", "31"]
        width = 0.35
        x = np.arange(len(labels))
        cmap = plt.get_cmap("Paired")(np.arange(10))

        fig, ax = plt.subplots()
        min_deg_bar = ax.bar(x - width / 2, min_deg_mean, width, label="Min-deg.", color=cmap[1])
        min_fill_bar = ax.bar(x + width / 2, min_fill_mean, width, label="Min-fill", color=cmap[0])

        ax.set_xticks([0, 1, 2, 3])
        ax.set_xticklabels(["3", "7", "15", "31"])
        ax.bar_label(min_deg_bar, padding=3)
        ax.bar_label(min_fill_bar, padding=3)
        ax.set_axisbelow(True)
        ax.grid()
        plt.legend()

        plt.title("Bar chart showing the runtime of each ordering \n heuristic for "
                  "binary tree shaped BNs of varying size")
        plt.xlabel("Number of nodes in the BN")
        plt.ylabel("Runtime (s)")
        plt.show()

    def test_bar_plot_sum_out_100(self):
        naive_mean, var_elim_mean = get_mean_runtime_data_split("./stats/stats_sum_out_100.json",
                                                                "naive", "var_elim")

        naive_mean.append(0)

        labels = ["3", "7", "15"]
        width = 0.35
        x = np.arange(len(labels))
        cmap = plt.get_cmap("Paired")(np.arange(10))

        fig, ax = plt.subplots()
        naive_bar = ax.bar(x - width / 2, naive_mean, width, label="Naive", color=cmap[3])
        var_elim_bar = ax.bar(x + width / 2, var_elim_mean, width, label="Var. elim.", color=cmap[2])

        ax.set_xticks([0, 1, 2])
        ax.set_xticklabels(labels)
        ax.bar_label(naive_bar, padding=3)
        ax.bar_label(var_elim_bar, padding=3)
        ax.set_axisbelow(True)
        ax.grid()
        plt.legend()

        plt.title("Bar chart showing the mean runtime of each summing out \n method for "
                  "binary tree shaped BNs of varying size.")
        plt.xlabel("Number of nodes in the BN")
        plt.ylabel("Runtime (s)")
        plt.show()


def load_json_data(file_path: Union[str, TextIO]):
    if isinstance(file_path, str):
        with open(file_path, "r") as file:
            return json.load(file)
    return json.load(file_path)


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


def get_runtime_data_split(file_ending: Tuple[str, str]):
    data_1 = []
    data_2 = []
    for file in os.listdir("results"):
        file_name = os.path.join("results", file)
        if file_name.endswith(file_ending[0]):
            data = load_json_data(file_name)
            data_1.append(data)
        if file.endswith(file_ending[1]):
            data = load_json_data(file_name)
            data_2.append(data)

    runtime_data_1 = [data["runtime"] for data in sorted(data_1, key=lambda k: k["bn_size"])]
    runtime_data_2 = [data["runtime"] for data in sorted(data_2, key=lambda k: k["bn_size"])]
    return runtime_data_1, runtime_data_2


def get_mean_runtime_data_split(file_path, data_type_1, data_type_2):
    data = load_json_data(file_path)
    mean_runtime_1 = [stat["runtime_stats"]["mean"] for stat in data if stat["type"] == data_type_1]
    mean_runtime_2 = [stat["runtime_stats"]["mean"] for stat in data if stat["type"] == data_type_2]
    return mean_runtime_1, mean_runtime_2


def set_boxplot_colors(bp, boxes="#FFFFFF", whiskers="#FFFFFF", caps="#FFFFFF", medians="#FFFFFF"):
    plt.setp(bp['boxes'], color=boxes)
    plt.setp(bp['whiskers'], color=whiskers)
    plt.setp(bp['caps'], color=caps)
    plt.setp(bp['medians'], color=medians)
