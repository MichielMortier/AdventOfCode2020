from file_handler import *


def solve(file_name):
    lines = FileHandler(file_name).get_file_lines()
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            if int(lines[i]) + int(lines[j]) == 2020:
                print(int(lines[i]) * int(lines[j]))


def solve2(file_name):
    lines = FileHandler(file_name).get_file_lines()
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            for k in range(j + 1, len(lines)):
                if int(lines[i]) + int(lines[j]) + int(lines[k]) == 2020:
                    print(int(lines[i]) * int(lines[j]) * int(lines[k]))
