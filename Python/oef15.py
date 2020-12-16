from file_handler import FileHandler
import functools
import time


def solve(file_name):
    lines = FileHandler(file_name).get_file_lines()
    mem = {}
    last_number = 0
    for index, number in enumerate(lines[0].split(",")):
        mem[int(number)] = int(index + 1)
        last_number = int(number)
    turn = len(lines[0].split(",")) + 1
    while turn <= 2020:
        if last_number in mem:
            # vorige turn en keer ervoor
            # print(turn - 1, "minus" ,mem[last_number])
            next_number = turn - 1 - mem[last_number]
        else:
            # print("new number found", last_number)
            next_number = 0
        # save 1 turn later
        mem[last_number] = turn - 1
        last_number = next_number
        # print(next_number)
        turn += 1
    print(last_number)


def solve2(file_name):
    beginTime = time.time()
    lines = FileHandler(file_name).get_file_lines()
    mem = {}
    last_number = 0
    for index, number in enumerate(lines[0].split(",")):
        mem[int(number)] = int(index + 1)
        last_number = int(number)
    turn = len(lines[0].split(",")) + 1
    while turn <= 30000000:
        if last_number in mem:
            # vorige turn en keer ervoor
            # print(turn - 1, "minus" ,mem[last_number])
            next_number = turn - 1 - mem[last_number]
        else:
            # print("new number found", last_number)
            next_number = 0
        # save 1 turn later
        mem[last_number] = turn - 1
        last_number = next_number
        # print(next_number)
        turn += 1
    endtime = time.time()
    print(endtime - beginTime)
    print(last_number)
