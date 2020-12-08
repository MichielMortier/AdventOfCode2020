from file_handler import FileHandler


def solve(file_name):
    lines = FileHandler(file_name).get_file_lines()
    instructions = []
    for line in lines:
        instructions.append([line[:3], int(line.split(" ")[1]), 0])
    acc, _ = find_loop(instructions)
    print(acc)


def solve2(file_name):
    lines = FileHandler(file_name).get_file_lines()
    instructions = []
    for index, line in enumerate(lines):
        instructions.append([line[:3], int(line.split(" ")[1]), 0, index])

    find_loop(instructions)

    possible_errors = list(filter(lambda element: element[2] == 1 and element[0] in ('jmp', 'nop'), instructions))
    for error in possible_errors:
        acc, current_instruction_pointer = init_and_correct_data(instructions, error)
        if current_instruction_pointer == len(instructions):
            print(acc)


def init_and_correct_data(instructions, error):
    # set truth table to zero
    for instruction in instructions:
        instruction[2] = 0

    instructions[error[3]][0] = ('nop' if instructions[error[3]][0] == 'jmp' else 'jmp')
    acc, current_instruction_pointer = find_loop(instructions)
    # revert change
    instructions[error[3]][0] = ('nop' if instructions[error[3]][0] == 'jmp' else 'jmp')
    return acc, current_instruction_pointer


def find_loop(instructions):
    acc = current_instruction_pointer = 0
    while current_instruction_pointer < len(instructions):
        next_instruction_pointer = current_instruction_pointer
        action = instructions[current_instruction_pointer][0]
        if action == 'acc':
            acc += instructions[current_instruction_pointer][1]
            next_instruction_pointer += 1
        elif action == 'jmp':
            next_instruction_pointer += instructions[current_instruction_pointer][1]
        else:
            next_instruction_pointer += 1
        instructions[current_instruction_pointer][2] = 1
        if next_instruction_pointer >= len(instructions):
            current_instruction_pointer = next_instruction_pointer
            break
        if instructions[next_instruction_pointer][2] == 1:
            break
        current_instruction_pointer = next_instruction_pointer
    return acc, current_instruction_pointer
