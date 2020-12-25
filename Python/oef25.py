input = ["12232269", "19452773"]

def solve(file_name):
    loop_size = []
    encryption_keys = []
    for number in input:
        value = 1
        turn = 0
        while value != int(number):
            value *= 7
            value %= 20201227
            turn += 1
        encryption_keys.append(value)
        loop_size.append(turn)
    value = 1
    for _ in range(0, loop_size[0]):
        value *= encryption_keys[1]
        value %= 20201227
