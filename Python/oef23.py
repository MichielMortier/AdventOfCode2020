input = "284573961"


def solve(file_name):
    numbers = [int(x) for x in input]
    input_len = len(numbers)
    max_number = max(numbers)
    turn = 0
    pointer = 0
    while turn < 100:
        pointer %= input_len
        print("-- move {} --".format(turn + 1))
        current_number = numbers[pointer]
        print("cups: {}, {}".format(numbers, current_number))
        destination_cup = numbers[pointer] - 1
        if pointer + 1 > (pointer + 4) % input_len:
            removed = [*numbers[pointer + 1:], *numbers[:(pointer + 4) % input_len]]
            del numbers[pointer + 1:]
            del numbers[:(pointer + 4) % input_len]
        else:
            removed = numbers[pointer + 1: pointer + 4]
            del numbers[pointer + 1: pointer + 4]
        print("pickup: {}".format(removed))
        while True:
            if destination_cup < 1:
                destination_cup = max_number
            try:
                numbers.index(destination_cup)
                break
            except:
                destination_cup -= 1
        print("destination: {}".format(destination_cup))
        index_number = (numbers.index(destination_cup) + 1) % input_len
        numbers[index_number: index_number] = removed
        pointer = numbers.index(current_number) + 1
        turn += 1
    print("Part 1: ", "".join(reversed("".join([str(i) for i in numbers]).split("1"))))


class Cup:
    def __init__(self, label: int) -> None:
        self.label = label
        self.next = None

    def __repr__(self):
        return f"Cup number: {self.label}"

# rip oplossing deel 1
def solve2(file_name):
    # linked list is de enige structuur die effecient genoeg is, zo vermijden we de index searches!!
    number_cups = 1000000
    labels = [int(l) for l in input]

    # Lege cups aanmaken
    lookup_table = {i: Cup(i) for i in range(1, number_cups + 1)}

    # Volgende zetten
    for i in range(1, number_cups):
        lookup_table[i].next = lookup_table[i + 1]

    lookup_table[number_cups].next = lookup_table[labels[0]]

    # eerste 9 goed zetten
    for i in range(len(labels)):
        lookup_table[labels[i]].next = lookup_table[labels[(i + 1) % len(labels)]]

    # laatste naar 1ste cup zetten, hier cup 2 dus
    if number_cups > len(labels):
        lookup_table[labels[-1]].next = lookup_table[len(labels) + 1]

    current_cup = lookup_table[labels[0]]

    for i in range(10000000):
        # 3 eerste verwijderen
        selection = current_cup.next
        current_cup.next = current_cup.next.next.next.next
        seek = current_cup.label - 1 if current_cup.label > 1 else number_cups
        while seek in [current_cup.label, selection.label, selection.next.label, selection.next.next.label]:
            seek -= 1
            if seek < 1:
                seek = number_cups

        next_cup = lookup_table[seek]
        selection.next.next.next = next_cup.next
        next_cup.next = selection
        current_cup = current_cup.next

    print("Part 2:", lookup_table[1].next.label * lookup_table[1].next.next.label)
