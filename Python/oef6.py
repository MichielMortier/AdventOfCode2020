from file_handler import FileHandler


def solve(file_name):
    lines = FileHandler(file_name).get_file_lines()
    answers = [[]]
    for line in lines:
        if line == '':
            answers.append(list())
        else:
            answers[-1].append(line)
    total_sum = 0
    for group_list in answers:
        count_answers = {}
        for element in group_list:
            for char in element:
                if char not in count_answers:
                    count_answers[char] = 1
                else:
                    count_answers[char] += 1
        total_sum += len(count_answers.keys())
    print(total_sum)


def solve2(file_name):
    lines = FileHandler(file_name).get_file_lines()
    answers = [[]]
    for line in lines:
        if line == '':
            answers.append(list())
        else:
            answers[-1].append(line)
    total_sum = 0
    for group_list in answers:
        count_answers = {}
        for element in group_list:
            for char in element:
                if char not in count_answers:
                    count_answers[char] = 1
                else:
                    count_answers[char] += 1
        for (_, value) in count_answers.items():
            if value == len(group_list):
                total_sum += 1
    print(total_sum)
