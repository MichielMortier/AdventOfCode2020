from file_handler import FileHandler


def solve(file_name):
    lines = FileHandler(file_name).get_file_lines()
    decoded = [
        int(line[:7].replace('F', '0').replace('B', '1'), 2) * 8 + int(line[7:].replace('R', '1').replace('L', '0'), 2)
        for line in lines]
    print(sorted(decoded))


def solve2(file_name):
    lines = FileHandler(file_name).get_file_lines()
    decoded = sorted([
        int(line[:7].replace('F', '0').replace('B', '1'), 2) * 8 + int(line[7:].replace('R', '1').replace('L', '0'), 2)
        for line in lines])
    for index in range(1, len(decoded)):
        if (decoded[index] - decoded[index - 1]) > 1:
            print("{} {}".format(decoded[index - 1], decoded[index]))
