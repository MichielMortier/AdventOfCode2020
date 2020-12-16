from file_handler import FileHandler
import re


def solve(file_name):
    lines = FileHandler(file_name).get_file_lines()
    i = 0
    numbers = list()
    while lines[i] != "":
        regex = re.match(".* (\d+)-(\d+) or (\d+)-(\d+)", lines[i])
        print(regex.group(1, 2, 3, 4))
        numbers += list(range(int(regex.group(1)), int(regex.group(2)) + 1))
        numbers += list(range(int(regex.group(3)), int(regex.group(4)) + 1))
        i += 1
    numbers = sorted(list(set(numbers)))
    total_sum = 0
    for line in lines[i:]:
        if line.count(",") != 0:
            for object_number in line.split(","):
                try:
                    numbers.index(int(object_number))
                except ValueError:
                    total_sum += int(object_number)
    print(total_sum)


def solve2(file_name):
    lines = FileHandler(file_name).get_file_lines()
    i = 0
    mapping_ranges = {}
    numbers = list()
    while lines[i] != "":
        regex = re.match("(.*): (\d+)-(\d+) or (\d+)-(\d+)", lines[i])
        mapping_ranges[regex.group(1)] = [int(regex.group(2)), int(regex.group(3)), int(regex.group(4)),
                                          int(regex.group(5))]
        numbers += list(range(int(regex.group(2)), int(regex.group(3)) + 1))
        numbers += list(range(int(regex.group(4)), int(regex.group(5)) + 1))
        i += 1
    numbers = sorted(list(set(numbers)))
    own_ticket = lines[i + 2]
    valid_fields = {}
    for line in lines[i:]:
        if line.count(",") != 0:
            try:
                for object_number in line.split(","):
                    numbers.index(int(object_number))
                for index, number in enumerate(line.split(",")):
                    if index in valid_fields:
                        valid_fields[index].append(int(number))
                    else:
                        valid_fields[index] = [int(number)]
            except ValueError:
                continue
    total_mul = 1
    while mapping_ranges:
        possible_fields = {names: [] for names in mapping_ranges}
        for ranges_of_fields in mapping_ranges:
            for index in valid_fields:
                correct = True
                for value in valid_fields[index]:
                    if not (mapping_ranges[ranges_of_fields][0] <= value <= mapping_ranges[ranges_of_fields][1] or \
                            mapping_ranges[ranges_of_fields][2] <= value <= mapping_ranges[ranges_of_fields][3]):
                        correct = False
                        break
                if correct:
                    possible_fields[ranges_of_fields].append(index)
        for poss in possible_fields:
            # if only 1 possible, it's that one
            if len(possible_fields[poss]) == 1:

                print(poss, possible_fields[poss][0])
                mapping_ranges.pop(poss)
                valid_fields.pop(possible_fields[poss][0])
                if re.match(".*departure.*", poss) is not None:
                    total_mul *= int(own_ticket.split(",")[possible_fields[poss][0]])
    print(total_mul)
