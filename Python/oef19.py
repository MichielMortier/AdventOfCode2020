from file_handler import FileHandler
import itertools
import re


def dp(rules, current_number):
    rule = rules[current_number]
    # rule contains no other rules
    if re.match(".*(\d).*", rule) is None:
        return
    else:
        total_rule = ""
        for concat_rule in rule.split(" | "):
            comb_list = []
            for sep_rule in concat_rule.split(" "):
                sep_rule = int(sep_rule)
                dp(rules, sep_rule)
                possible_combs = rules[sep_rule].split(" | ")
                comb_list.append(possible_combs)
            for element in itertools.product(*comb_list):
                element = "".join(element)
                total_rule += element + " | "
        total_rule = total_rule.rstrip(" | ")
        rules[current_number] = total_rule
        print(current_number, total_rule)


def parse_rules(rule_id, rules):
    if rule_id in "ab|":
        return rule_id
    sub_rules = rules[rule_id].split(' ')
    if rule_id in sub_rules:
        if len(sub_rules) == 4:
            return "" + parse_rules(sub_rules[0], rules) + "+"
        elif len(sub_rules) == 6:
            generated_rules = []
            for i in range(1, 5):  # Handling only 5 depths of recursion for speed - dataset only goes this deep
                generated_rules.append(
                    f"({parse_rules(sub_rules[0], rules)}{{{i}}}{parse_rules(sub_rules[1], rules)}{{{i}}})")
            return "(" + '|'.join(generated_rules) + ")"
    new_rules = ''.join([parse_rules(x, rules) for x in sub_rules])
    return new_rules if len(new_rules) == 1 or "|" not in new_rules else \
        "(" + ''.join([parse_rules(x, rules) for x in sub_rules]) + ")"


def solve(file_name):
    lines = FileHandler(file_name).get_file_lines()
    rules = {}
    for line in lines:
        if line == "":
            break
        number, rule = line.split(": ")
        rules[int(number)] = (rule.strip("\""))
    strings = lines[len(rules) + 1:]
    dp(rules, 0)
    for index in rules:
        rules[index] = rules[index].split(" | ")
    total = 0
    for string in strings:
        try:
            rules[0].index(string)
            total += 1
        except:
            pass
    print(total)


def rules_to_dict(raw_rules: str, rules) -> None:
    for raw_rule in raw_rules.split("\n"):
        number, rule = raw_rule.split(': ')
        rules[number] = rule.strip('"')


def solve2(file_name):
    rules = {}
    raw_rules, messages = open(file_name).read().split('\n\n')
    rules_to_dict(raw_rules, rules)
    all_rules = re.compile("^" + parse_rules("0", rules) + "$")
    total = sum((int(all_rules.match(m) is not None) for m in messages.split("\n")))
    print(f"Total matches: {total}")
