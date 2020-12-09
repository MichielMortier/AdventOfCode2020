from file_handler import FileHandler


def check_if_sum_exists(current_perm, current_sum):
    for i in range(len(current_perm)):
        for j in range(i + 1, len(current_perm)):
            if current_perm[i] + current_perm[j] == current_sum:
                return True
    return False


def solve(file_name):
    lines = FileHandler(file_name).get_file_lines()
    all_numbers = [int(line) for line in lines]
    current_perm = all_numbers[:25]
    all_numbers = all_numbers[25:]
    while len(all_numbers) > 0:
        current_sum = all_numbers.pop(0)
        if check_if_sum_exists(current_perm, current_sum):
            current_perm.pop(0)
            current_perm.append(current_sum)
        else:
            print(current_sum)
            break


def findCombination(current_perm, total_sum):
    for index in range(len(current_perm)):
        i = 1
        while total_sum > sum(current_perm[index:i]):
            i += 1
        if total_sum == sum(current_perm[index:i]):
            print(min(current_perm[index:i]) + max(current_perm[index:i]))
            break


def solve2(file_name):
    lines = FileHandler(file_name).get_file_lines()
    all_numbers = [int(line) for line in lines]
    current_perm = all_numbers[:25]
    all_numbers = all_numbers[25:]
    current_sum = 0
    while len(all_numbers) > 0:
        current_sum = all_numbers.pop(0)
        if check_if_sum_exists(current_perm, current_sum):
            current_perm.pop(0)
            current_perm.append(current_sum)
        else:
            print(current_sum)
            break
    all_numbers = [int(line) for line in lines]
    findCombination(all_numbers, current_sum)

