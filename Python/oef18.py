from file_handler import FileHandler
import re

actions = {'+': lambda a, b: a + b, '*': lambda a, b: a * b}


def evaluate_brackets(splitted):
    while len(splitted) > 1:
        # first bracket already popped off
        left_element = splitted.pop(0)
        if left_element == '(':
            left_element = evaluate_brackets(splitted)
        operant = splitted.pop(0)
        if operant == ')':
            return left_element
        right_element = splitted.pop(0)
        if right_element == '(':
            right_element = evaluate_brackets(splitted)
        total = actions[operant](int(left_element), int(right_element))
        if len(splitted) > 0 and splitted[0] == ')':
            splitted.pop(0)
            return total
        else:
            splitted.insert(0, total)
    return splitted[0]

def solve(file_name):
    lines = FileHandler(file_name).get_file_lines()
    sum = 0

    for evaluation in lines:
        splitted = re.split("(\D)", evaluation.replace(" ", ""))
        splitted = [split for split in splitted if split != '']
        sum += evaluate_brackets(splitted)
    print(sum)


def is_int(integer):
    try:
        int(integer)
        return True
    except:
        return False

def evaluate_brackets_2(splitted):
    while len(splitted) > 1:
        # first bracket already popped off
        left_element = splitted.pop(0)
        if left_element == '(':
            left_element = evaluate_brackets_2(splitted)
            splitted.pop(0) # ) pop
            if len(splitted) == 0:
                return left_element
        operant = splitted.pop(0)
        if operant == ')':
            splitted.insert(0, ')')
            return left_element
        if operant == '*':
            right_element = evaluate_brackets_2(splitted)
        else:
            right_element = splitted.pop(0)
        if right_element == '(':
            right_element = evaluate_brackets_2(splitted)
            splitted.pop(0) # ) pop
        total = actions[operant](int(left_element), int(right_element))
        if len(splitted) > 0 and splitted[0] == ')':
            return total
        else:
            if len(splitted) == 0:
                return total
            splitted.insert(0, total)
    return splitted.pop(0)


def evaluate_mult(splitted):
    while len(splitted) > 1:
        pass
    return splitted[0]


def solve2(file_name):
    lines = FileHandler(file_name).get_file_lines()
    sum = 0

    for evaluation in lines:
        splitted = re.split("(\D)", evaluation.replace(" ", ""))
        splitted = [split for split in splitted if split != '']
        sum += evaluate_brackets_2(splitted)
    print(sum)
