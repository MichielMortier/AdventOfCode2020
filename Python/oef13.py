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
    all_buses = [time for time in lines[1].split(',')]
    offset = {}
    for number in all_buses:
        if represents_int(number):
            offset[int(number)] = all_buses.index(number)
    print(find_Y(offset))
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

    # Chinese Remainder Theorem is de efficient manier om dit op te lossen met een algoritme


# Chinese Remainder theorem implementation
def find_Y(mod_and_rest_combination):
    for number in mod_and_rest_combination:
        mod_and_rest_combination[number] = (number - mod_and_rest_combination[number]) % number
    print(mod_and_rest_combination)
    # eerst zoeken we M, de totale modulo die we op het einde moeten nemen om Y te vinden
    # Y = R mod M
    # M is multiplication van alle mods
    M = functools.reduce(lambda a, b: a * b, list(mod_and_rest_combination.keys()))
    # nu zoeken we de componeten voor R
    # R is de som van alle mx * mx' * restx
    # mx is M/modx
    mx = [M / modx for modx in mod_and_rest_combination.keys()]
    # mx' is (mx)^-1 mod nx
    mx_accent = [mul_inv(mx_element, modx) for (mx_element, modx) in zip(mx, mod_and_rest_combination.keys())]

    # again: R is de som van alle mx * mx' * restx
    R = sum([mx_element * mx_accent_element * restx for mx_element, mx_accent_element, restx in
             zip(mx, mx_accent, mod_and_rest_combination.values())])
    Y = R % M
    return Y

# inverse module zoeken:
# a mod b -> inverse is ax mod b = 1 => zoek x
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1