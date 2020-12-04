from file_handler import *
import numpy as np
from functools import reduce


def solve(file_name):
    lines = FileHandler(file_name).get_file_lines()
    path = np.zeros(shape=(len(lines), len(lines[0])))
    for index, line in enumerate(lines):
        line = " ".join(line.replace('.', '0').replace('#', '1'))
        print(line)
        path[index] = np.fromstring(line, dtype=int, sep=' ')
    total_sum = count_tree_on_path(path, (1, 3))
    print(total_sum)


def solve2(file_name):
    lines = FileHandler(file_name).get_file_lines()
    path = np.zeros(shape=(len(lines), len(lines[0])))
    for index, line in enumerate(lines):
        line = " ".join(line.replace('.', '0').replace('#', '1'))
        path[index] = np.fromstring(line, dtype=int, sep=' ')
    total_list = list()
    for movement in ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1)):
        total_list.append(count_tree_on_path(path, movement))
    print(reduce(lambda a, b: a * b, total_list))


def count_tree_on_path(path, movement):
    i = j = 0
    total_sum = 0
    i_shape, j_shape = path.shape
    while i < i_shape:
        j %= j_shape
        total_sum += path[i][j]
        i += movement[0]
        j += movement[1]
    return total_sum
