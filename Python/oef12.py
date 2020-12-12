from file_handler import FileHandler
import math

directions = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}


def get_forward_movement(direction, steps):
    return [direction[0] * steps, direction[1] * steps]


def rotate_vector(vector, degrees):
    # point rotation x' = x*cos(a) - y * sin(a) y' = y*cos(a) + x*sin(a)
    return [
        vector[0] * int(math.cos(math.radians(degrees))) - vector[1] * int(math.sin(math.radians(degrees)))
        , vector[1] * int(math.cos(math.radians(degrees))) + vector[0] * int(math.sin(math.radians(degrees)))]


def solve(file_name):
    lines = FileHandler(file_name).get_file_lines()
    start_position = [0, 0]
    face_direction = (0, 1)
    for line in lines:
        direction, steps = (line[0], int(line[1:]))
        if direction in directions:
            start_position = [x + y for x, y in zip(get_forward_movement(directions[direction], steps), start_position)]
        elif direction == 'F':
            start_position = [x + y for x, y in zip(get_forward_movement(face_direction, steps), start_position)]
        else:
            if direction == 'R':
                steps = 360 - steps
            face_direction = rotate_vector(face_direction, steps)
    print(math.fabs(start_position[0]) + math.fabs(start_position[1]))


def solve2(file_name):
    lines = FileHandler(file_name).get_file_lines()
    start_position = [0, 0]
    start_vector = [10, 1]
    for line in lines:
        direction, steps = (line[0], int(line[1:]))
        if direction in directions:
            start_vector = [x + y for x, y in zip(get_forward_movement(directions[direction], steps), start_vector)]
        elif direction == 'F':
            start_position = [x + y for x, y in zip(get_forward_movement(start_vector, steps), start_position)]
        else:
            if direction == 'R':
                steps = 360 - steps
            start_vector = rotate_vector(start_vector, steps)
    print(math.fabs(start_position[0]) + math.fabs(start_position[1]))
