import numpy as np
import copy

direction = {"ne": [-1, 1], "nw": [-1, -1], "se": [1, 1], "sw": [1, -1], "e": [0, 2], "w": [0, -2]}


def sum_black_tiles(tiles, i, j):
    return np.sum(tiles[max(0, i - 1):i + 2, max(0, j - 2):j + 3]) - tiles[i, j]


def solve(file_name):
    np.set_printoptions(threshold=np.inf)

    commands = open(file_name).read().split("\n")
    tile_structure = np.zeros(shape=(300, 300), dtype='int8')

    for command in commands:
        start_point = [150, 150]
        while command:
            if command[0] in ('s', 'n'):
                current_command = command[0:2]
                command = command[2:]
            else:
                current_command = command[0]
                command = command[1:]
            for index, number in enumerate(direction[current_command]):
                start_point[index] += number
        tile_structure[start_point[0], start_point[1]] = (tile_structure[start_point[0], start_point[1]] + 1) % 2
    print("Part 1:", np.sum(tile_structure))
    # for line in tile_structure:
    #     print("".join([str(x) for x in line]))
    # print()
    turn = 0
    while turn < 100:
        copy_tile = copy.deepcopy(tile_structure)
        for i in range(0, tile_structure.shape[0]):
            for j in range(i%2, tile_structure.shape[1], 2):
                som = sum_black_tiles(tile_structure, i, j)
                if tile_structure[i, j] and (som == 0 or som > 2):
                    copy_tile[i, j] = 0
                if not tile_structure[i, j] and som == 2:
                    copy_tile[i, j] = (tile_structure[i, j] + 1) % 2
        tile_structure = copy_tile
        # for line in tile_structure:
        #     print("".join([str(x) for x in line]))
        print("Day ", turn + 1, ": ", np.sum(tile_structure))
        turn += 1