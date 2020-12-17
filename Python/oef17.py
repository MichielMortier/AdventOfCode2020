from file_handler import FileHandler
import numpy as np
import sys
import copy


def getsumofneighbors(matrix, i, j, k):
    region = matrix[max(0, i - 1): i + 2, max(0, j - 1): j + 2, max(0, k - 1): k + 2]
    return np.sum(region) - matrix[i, j, k]  # Sum the region and subtract center


def solve(file_name):
    number_of_cycles = 6
    np.set_printoptions(threshold=sys.maxsize)
    lines = FileHandler(file_name).get_file_lines()
    max_size = len(lines) + 2 * number_of_cycles
    matrix = np.zeros(shape=(max_size, max_size, 1 + 2 * number_of_cycles))
    print(matrix.shape)
    for index, line in enumerate(lines):
        line = " ".join(number_of_cycles * '0' + line.replace('.', '0').replace('#', '1') + number_of_cycles * '0')
        matrix[index + number_of_cycles, :, number_of_cycles] = np.fromstring(line, dtype=int, sep=' ')
    for a in range(0, number_of_cycles):  #
        copy_matrix = copy.deepcopy(matrix)
        for i in range(number_of_cycles - a - 1, matrix.shape[0] - (number_of_cycles - a) + 1):
            for j in range(number_of_cycles - a - 1, matrix.shape[1] - (number_of_cycles - a) + 1):
                for k in range(number_of_cycles - a - 1, matrix.shape[2] - (number_of_cycles - a) + 1):
                    total_sum = getsumofneighbors(matrix, i, j, k)
                    if matrix[i, j, k] == 1 and not (2 <= total_sum <= 3):
                        copy_matrix[i, j, k] = 0
                    if matrix[i, j, k] == 0 and total_sum == 3:
                        copy_matrix[i, j, k] = 1
        matrix = copy.deepcopy(copy_matrix)
        for x in range(number_of_cycles - a - 1, matrix.shape[2] - (number_of_cycles - a) + 1):
            print(matrix[(number_of_cycles - a - 1): (matrix.shape[0] - (number_of_cycles - a) + 1),
                  (number_of_cycles - a - 1): (matrix.shape[1] - (number_of_cycles - a) + 1)
                  , x])
    print(np.sum(matrix))


def getsumofneighbors_4(matrix, i, j, k, w):
    region = matrix[max(0, i - 1): i + 2, max(0, j - 1): j + 2, max(0, k - 1): k + 2, max(0, w - 1): w + 2]
    return np.sum(region) - matrix[i, j, k, w]  # Sum the region and subtract center


def solve2(file_name):
    number_of_cycles = 6
    np.set_printoptions(threshold=sys.maxsize)
    lines = FileHandler(file_name).get_file_lines()
    max_size = len(lines) + 2 * number_of_cycles
    matrix = np.zeros(shape=(max_size, max_size, 1 + 2 * number_of_cycles, 1 + 2 * number_of_cycles))
    print(matrix.shape)
    for index, line in enumerate(lines):
        line = " ".join(number_of_cycles * '0' + line.replace('.', '0').replace('#', '1') + number_of_cycles * '0')
        matrix[index + number_of_cycles, :, number_of_cycles, number_of_cycles] = np.fromstring(line, dtype=int,
                                                                                                sep=' ')
    for a in range(0, number_of_cycles):  #
        copy_matrix = copy.deepcopy(matrix)
        for i in range(number_of_cycles - a - 1, matrix.shape[0] - (number_of_cycles - a) + 1):
            for j in range(number_of_cycles - a - 1, matrix.shape[1] - (number_of_cycles - a) + 1):
                for k in range(number_of_cycles - a - 1, matrix.shape[2] - (number_of_cycles - a) + 1):
                    for w in range(number_of_cycles - a - 1, matrix.shape[3] - (number_of_cycles - a) + 1):
                        total_sum = getsumofneighbors_4(matrix, i, j, k, w)
                        if matrix[i, j, k, w] == 1 and not (2 <= total_sum <= 3):
                            copy_matrix[i, j, k, w] = 0
                        if matrix[i, j, k, w] == 0 and total_sum == 3:
                            copy_matrix[i, j, k, w] = 1
        matrix = copy.deepcopy(copy_matrix)
        # for x in range(number_of_cycles - a - 1, matrix.shape[2] - (number_of_cycles - a) + 1):
        #     print(matrix[(number_of_cycles - a - 1): (matrix.shape[0] - (number_of_cycles - a) + 1),
        #           (number_of_cycles - a - 1): (matrix.shape[1] - (number_of_cycles - a) + 1)
        #           ,  x])
    print(np.sum(matrix))
