from file_handler import FileHandler


def solve(file_name):
    getParent = dict()
    lines = FileHandler(file_name).get_file_lines()
    for line in lines:
        identifier, rest = line.split(" contain ")
        identifier = "".join(identifier.split(" ")[:2])
        content = rest.strip(".").split(", ")
        bags_inside = []
        for bag in content:
            if content != 'no other bags':
                number_of, name = bag.split(" ", 1)
                name = "".join(name.split(" ")[:2])
                bags_inside.append((number_of, name))
                if name in getParent.keys():
                    getParent[name].append(identifier)
                else:
                    getParent[name] = [identifier]
    queue = ['shinygold']
    total_list = list()
    while queue:
        name = queue.pop(0)
        if name in getParent:
            queue = queue + getParent[name]
            total_list = total_list + getParent[name]
    print(len(set(total_list)))


def solve2(file_name):
    bag_contains = dict()
    lines = FileHandler(file_name).get_file_lines()
    for line in lines:
        identifier, rest = line.split(" contain ")
        identifier = "".join(identifier.split(" ")[:2])
        content = rest.strip(".").split(", ")
        bags_inside = []
        for bag in content:
            if bag != 'no other bags':
                number_of, name = bag.split(" ", 1)
                name = "".join(name.split(" ")[:2])
                bags_inside.append((number_of, name))
        if bags_inside:
            bag_contains[identifier] = bags_inside

    number_of_bags = count_bags('shinygold', bag_contains) - 1
    print(number_of_bags)


def count_bags(bag_name, bag_contains, total_sum=0, factor=1):
    if bag_name in bag_contains:
        sum = 0
        for (count, name) in bag_contains[bag_name]:
            print(name, count, factor)
            sum += count_bags(name, bag_contains, total_sum, factor * int(count)) * int(count)
        sum += 1
        return sum
    else:
        return 1
