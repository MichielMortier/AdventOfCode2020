import re
import copy
import numpy as np
import regex


def rotate_full_tile(tile, sides):
    while sides[0] != '' and sides[0] != find_pattern(0, tile) and sides[0] != find_pattern(0, tile)[::-1]:
        tile = np.rot90(tile, 1)
        if sides[0] == find_pattern(0, tile)[::-1]:
            tile = np.flipud(tile)
    return tile


def find_pattern(index_to_go, tile):
    if index_to_go == 0:
        pattern = tile[0, :]
    elif index_to_go == 1:
        pattern = tile[:, -1]
    elif index_to_go == 2:
        pattern = tile[-1, :]
    else:
        pattern = tile[:, 0]
    return "".join(pattern)


# reverse is -1 or 1
def rotate_tile(tile, current_index, index_to_go, pattern_to_match):
    # do rotation to bring current side to the side we need => e g size on index 1  needs to be on index 2
    for _ in range(0, ((index_to_go - current_index) % 4)):
        copy_tile = copy.deepcopy(tile)
        tile[0] = copy_tile[3][::-1]
        tile[1] = copy_tile[0][::1]
        tile[2] = copy_tile[1][::-1]
        tile[3] = copy_tile[2][::1]
    # it the pattern does not match, we need to inverse the pattern
    if pattern_to_match != tile[index_to_go]:
        tile[index_to_go] = tile[index_to_go][::-1]
        tile[index_to_go - 2] = tile[index_to_go - 2][::-1]
        tile[(index_to_go - 1) % 4], tile[(index_to_go + 1) % 4] = tile[(index_to_go + 1) % 4], tile[
            (index_to_go - 1) % 4]
    return tile


def set_place_in_array(tile_location, reverse_lookup, tid, index_to_place, index):
    coords = get_offset_coords(reverse_lookup, tid, index)
    tile_location[coords[0], coords[1]] = index_to_place
    reverse_lookup[index_to_place] = (coords[0], coords[1])


# if current tile is connected it the side INDEX of tile with id TID
def get_offset_coords(reverse_lookup, tid, index):
    coords = reverse_lookup[tid]
    if index == 0:
        return coords[0] - 1, coords[1]
    elif index == 1:
        return coords[0], coords[1] + 1
    elif index == 2:
        return coords[0] + 1, coords[1]
    elif index == 3:
        return coords[0], coords[1] - 1


def check_with_already_placed_tiles_neighbours(correct_rotation, tile_placed, tile_location, reverse_lookup, tid,
                                               index):
    x, y = get_offset_coords(reverse_lookup, tid, index)
    correct = True
    # there is tile on top of the new one
    if tile_location[x - 1, y] != 0:
        # so bottom part should match the new tile top side
        correct = correct and (tile_placed[tile_location[x - 1, y]][2] == correct_rotation[0])
    if tile_location[x + 1, y] != 0:
        correct = correct and (tile_placed[tile_location[x + 1, y]][0] == correct_rotation[2])
    if tile_location[x, y - 1] != 0:
        correct = correct and (tile_placed[tile_location[x, y - 1]][1] == correct_rotation[3])
    if tile_location[x, y + 1] != 0:
        correct = correct and (tile_placed[tile_location[x, y + 1]][3] == correct_rotation[1])
    return correct


def remove_filled_sides(correct_rotation, tile_placed, tile_location, reverse_lookup, tid,
                        index):
    x, y = get_offset_coords(reverse_lookup, tid, index)
    # there is tile on top of the new one
    if tile_location[x - 1, y] != 0:
        # so bottom part should match the new tile top side
        tile_placed[tile_location[x - 1, y]][2] = ''
        correct_rotation[0] = ''
    if tile_location[x + 1, y] != 0:
        tile_placed[tile_location[x + 1, y]][0] = ''
        correct_rotation[2] = ''
    if tile_location[x, y - 1] != 0:
        tile_placed[tile_location[x, y - 1]][1] = ''
        correct_rotation[3] = ''
    if tile_location[x, y + 1] != 0:
        tile_placed[tile_location[x, y + 1]][3] = ''
        correct_rotation[1] = ''
    return correct_rotation


def solve(file_name):
    np.set_printoptions(threshold=np.inf)
    tiles = open(file_name).read().split("\n\n")[:-1]
    tile_collection = {}
    for tile in tiles:
        title, *rest = tile.split("\n")
        title = int(re.search(r'(\d+)', title).group(1))
        tile_collection[title] = rest
    tile_poss = {}
    # bovenkant = 0, rechts = 1; onder 2; links 3
    for tid in tile_collection:
        tile_edge = [tile_collection[tid][0], tile_collection[tid][-1]]  # boven en onder
        left_side = "".join([line[0] for line in tile_collection[tid]])
        right_side = "".join([line[-1] for line in tile_collection[tid]])
        tile_edge.insert(1, right_side)
        tile_edge.append(left_side)
        tile_poss[tid] = tile_edge
    first_key = list(tile_poss.keys())[0]
    tile_location = np.zeros(shape=(50, 50), dtype=int)
    tile_placed = {first_key: tile_poss[first_key]}
    tile_saved_sides = {first_key: tile_poss[first_key]}
    tile_location[25, 25] = first_key
    reverse_lookup = {first_key: (25, 25)}
    tile_poss.pop(first_key)
    while len(tile_poss.keys()) > 0:
        # try tile from not placed tiles
        for current_tile_id in tile_poss:
            placed = False
            current_tile = copy.deepcopy(tile_poss[current_tile_id])
            # Get all placed tile, to look for a match between unfilled sides
            for tid in tile_placed:
                # loop over all possible sides of the placed tile
                for index, side in enumerate(tile_placed[tid]):
                    # side == '' if already matched
                    if side != '':
                        # iter over all sides of the current tile
                        for index_to_place, tile_to_place_side in enumerate(current_tile):
                            if side == tile_to_place_side or side == tile_to_place_side[::-1]:
                                # save current rotation of the tile in the placed collection
                                # we starten bv op index 2 => maar de zijde moet naar index 1 omdat index gematcht aan zijde 3 ligt
                                correct_rotation = rotate_tile(current_tile, index_to_place,
                                                                                    (index + 2) % 4, side)
                                if check_with_already_placed_tiles_neighbours(correct_rotation, tile_placed,
                                                                              tile_location,
                                                                              reverse_lookup, tid, index):
                                    # tile matches side
                                    tile_poss.pop(current_tile_id)
                                    tile_saved_sides[current_tile_id] = copy.deepcopy(correct_rotation)
                                    correct_rotation = remove_filled_sides(correct_rotation, tile_placed,
                                                                           tile_location,
                                                                           reverse_lookup, tid, index)
                                    set_place_in_array(tile_location, reverse_lookup, tid, current_tile_id, index)
                                    tile_placed[current_tile_id] = correct_rotation
                                    placed = True
                                    break
                    if placed:
                        break
                if placed:
                    break
            if placed:
                break
    cleaned_tile_location = []
    for line in tile_location:
        lijst = [supp for supp in line if supp != 0]
        if lijst:
            cleaned_tile_location.append(lijst)
    print("Part 1: ", cleaned_tile_location[0][0] * cleaned_tile_location[0][-1] * cleaned_tile_location[-1][0] * cleaned_tile_location[-1][-1])
    for tile in tile_collection:
        array_tile = np.array([[char for char in xi] for xi in tile_collection[tile]])
        array_tile = rotate_full_tile(array_tile, tile_saved_sides[tile])
        array_tile = array_tile[1:-1, 1:-1]
        tile_collection[tile] = array_tile
    total_tiles = None
    for locations in cleaned_tile_location:
        supp_total = None
        for tid in locations:
            if supp_total is None:
                supp_total = tile_collection[tid]
            else:
                supp_total = np.concatenate((supp_total, tile_collection[tid]), axis=1)
        if total_tiles is None:
            total_tiles = supp_total
        else:
            total_tiles = np.concatenate((total_tiles, supp_total), axis=0)
    for index in range(0,4):
        rotation = np.rot90(total_tiles, index)
        rotation = np.flipud(rotation)
        image = "\n".join("".join(horizontal_tile) for horizontal_tile in rotation)
        spacing = '[.#\n]{77}'
        monster = f'#.{spacing + "#....#" * 3}##{spacing}.#{"..#" * 5}'

        m = len(regex.findall(monster, image, overlapped=True))
        if m:
            print('Part 2:', sum(c == '#' for c in image) - 15 * m)