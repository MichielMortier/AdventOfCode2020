from file_handler import *


def solve(file_name):
    lines = FileHandler(file_name).get_file_lines()
    count = 0
    for line in lines:
        (numberOfTimes, char, password) = line.split(" ")
        (min_number, max_number) = numberOfTimes.split("-")
        char = char.strip(":")
        # print("{} {} {}".format(int(min_number), password.count(char), int(max_number)))
        if int(min_number) <= password.count(char) <= int(max_number):
            count += 1
    print(count)


def solve2(file_name):
    lines = FileHandler(file_name).get_file_lines()
    count = 0
    for line in lines:
        (numberOfTimes, char, password) = line.split(" ")
        (min_number, max_number) = numberOfTimes.split("-")
        char = char.strip(":")
        # print("{} {} {}".format(int(min_number), password.count(char), int(max_number)))
        if bool(password[int(min_number) - 1] == char) != bool(password[int(max_number) - 1] == char):
            print("{} {} {} {}".format(int(min_number), int(max_number), char ,password))
            count += 1
    print(count)
