from file_handler import FileHandler
import functools


def solve(file_name):
    lines = FileHandler(file_name).get_file_lines()
    number_of_minutes = int(lines[0])
    all_buses = [int(time) for time in lines[1].split(',') if time != 'x']
    max_for_bus = {}
    for bus in all_buses:
        next_stop = 0
        while next_stop < number_of_minutes:
            next_stop += bus
            if next_stop > number_of_minutes and (
                    bus not in max_for_bus or max_for_bus[bus] > next_stop - number_of_minutes):
                max_for_bus[bus] = next_stop - number_of_minutes
    print(sorted(max_for_bus.items(), key=lambda a: a[1])[0])


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def solve2(file_name):
    lines = FileHandler(file_name).get_file_lines()
    number_of_minutes = int(lines[0])
    all_buses = [time for time in lines[1].split(',')]
    offset = {}
    for number in all_buses:
        if represents_int(number):
            offset[int(number)] = all_buses.index(number)
    # highest_number = max(filter(lambda x: represents_int(x), all_buses))
    # highest_number_offset = offset[int(highest_number)]
    # for number in offset:
    #     offset[number] = offset[number] - highest_number_offset

    # counter = 0
    # while True:
    #     counter += int(highest_number)
    #     is_not_correct = False
    #     for off in offset:
    #         if ((counter+offset[off]) % off) != 0:
    #             is_not_correct = True
    #             break
    #     if not is_not_correct:
    #         break
    # print(counter-highest_number_offset)

    # for number, off in offset.items():
    #     print("{} /  t + {}".format(number, off))
    #     # wanneer we 23 toevoegen, zien we dat er meerdere modulos 0 worden, dit wil zeggen dat we t' = t + 23 kunnen doen
    #     # op deze manier weten we dat het getal een veelvoud is van 23, 421, 17, 19 en 29! (
    #     print("t mod {} = {}".format(number, (number - off + list(offset.keys())[0]) % number))

    mod_nul_lijst = [number for number, off in offset.items() if (number - off + list(offset.keys())[0]) % number == 0]
    for off in offset:
        offset[off] = (offset[off] - list(offset.keys())[0]) % off
    for number, off in offset.items():
        print("t' mod {} = {}".format(number, off))
    print(mod_nul_lijst)
    multiply = functools.reduce(lambda a, b: a * b, mod_nul_lijst)
    print(multiply)
    counter = 0
    # brute force
    while True:
        counter += multiply
        is_not_correct = False
        for off in offset:
            if ((counter + offset[off]) % off) != 0:
                is_not_correct = True
                break
        if not is_not_correct:
            break
    print(counter - list(offset.keys())[0])
