from file_handler import FileHandler
import itertools


def fill_empty(seats):
    copy = [x.copy() for x in seats]
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            if seats[i][j] == 'L':
                count = 0
                for k, w in itertools.product(range(i - 1, i + 2), range(j - 1, j + 2)):
                    if k == i and w == j:
                        continue
                    if -1 < k < len(seats) and -1 < w < len(seats[i]):
                        count += 1 if seats[k][w] == '#' else 0
                if count == 0:
                    copy[i][j] = '#'
    return copy


def remove_occupied(seats):
    copy = [x.copy() for x in seats]
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            if seats[i][j] == '#':
                count = 0
                for k, w in itertools.product(range(i - 1, i + 2), range(j - 1, j + 2)):
                    if k == i and w == j:
                        continue
                    if -1 < k < len(seats) and -1 < w < len(seats[i]):
                        count += 1 if seats[k][w] == '#' else 0
                if count >= 4:
                    copy[i][j] = 'L'
    return copy


def long_check(i, j, seats):
    count = 0
    for increment_i, increment_j in ((-1, -1), (-1, 1), (1, -1), (1, 1), (0, 1), (1, 0), (0, -1), (-1, 0)):
        k = i + increment_i
        w = j + increment_j
        while is_not_out_of_array(k, w, seats) and seats[k][w] == '.':
            k += increment_i
            w += increment_j
        if is_not_out_of_array(k, w, seats):
            count += 1 if seats[k][w] == '#' else 0
    return count


def fill_empty2(seats):
    copy = [x.copy() for x in seats]
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            if seats[i][j] == 'L':
                count = 0
                count += long_check(i, j, seats)
                if count == 0:
                    copy[i][j] = '#'
    return copy


def remove_occupied2(seats):
    copy = [x.copy() for x in seats]
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            if seats[i][j] == '#':
                count = long_check(i, j, seats)
                if count >= 5:
                    copy[i][j] = 'L'
    return copy


def is_not_out_of_array(k, w, seats):
    return -1 < k < len(seats) and -1 < w < len(seats[0])


def solve(file_name):
    lines = FileHandler(file_name).get_file_lines()
    seats = []
    for line in lines:
        seats.append([c for c in line.strip()])
    prev_count = 0
    while True:
        seats = fill_empty(seats)
        seats = remove_occupied(seats)
        total_count = 0
        for seat_row in seats:
            total_count += seat_row.count('#')
        if total_count == prev_count:
            break
        prev_count = total_count
    end = 0
    for seat_row in seats:
        end += seat_row.count('#')
    print(end)


def solve2(file_name):
    lines = FileHandler(file_name).get_file_lines()
    seats = []
    for line in lines:
        seats.append([c for c in line.strip()])
    prev_count = 0
    while True:
        seats = fill_empty2(seats)
        seats = remove_occupied2(seats)
        total_count = 0
        for seat_row in seats:
            total_count += seat_row.count('#')
        if total_count == prev_count:
            break
        prev_count = total_count
    end = 0
    for seat_row in seats:
        end += seat_row.count('#')
    print(end)
