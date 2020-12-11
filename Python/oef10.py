from file_handler import FileHandler


def solve(file_name):
    lines = FileHandler(file_name).get_file_lines()
    all_jolts = [int(line) for line in lines]
    diff_counter = {}
    all_jolts.sort()
    all_jolts.append(all_jolts[-1] + 3)
    previous_jolt = 0
    for jolt in all_jolts:
        diff = jolt - previous_jolt
        if diff in diff_counter:
            diff_counter[diff] += 1
        else:
            diff_counter[diff] = 1
        previous_jolt = jolt
    print(diff_counter)


def solve2(file_name):
    lines = FileHandler(file_name).get_file_lines()
    all_jolts = [int(line) for line in lines]
    all_jolts.sort()
    all_jolts.insert(0,0)
    all_jolts.append(all_jolts[-1] + 3)
    possible = {}
    number_of_paths = {}
    for jolts in all_jolts:
        possible[jolts] = get_possible_jolts(jolts, all_jolts)
        number_of_paths[jolts] = 0
    number_of_paths[all_jolts[-1]] = 1

    for jolts in reversed(all_jolts[:-1]):
        number_of_paths[jolts] = sum([number_of_paths[poss] for poss in possible[jolts]])
    print(number_of_paths[0])


# to long...
def back_tracking(previous_jolt, all_jolts, total_count):
    possible = get_possible_jolts(previous_jolt, all_jolts)
    while possible:
        poss = possible.pop(0)
        if poss + 3 == all_jolts[-1]:
            total_count += 1
        else:
            total_count = back_tracking(poss, all_jolts, total_count)
    return total_count


def get_possible_jolts(previousJolt, allJolts):
    return list(filter(lambda x: previousJolt < x <= previousJolt + 3, allJolts))
