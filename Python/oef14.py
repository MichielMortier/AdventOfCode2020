from file_handler import FileHandler
import functools


def solve(file_name):
    lines = FileHandler(file_name).get_file_lines()
    mem = {}
    mask = None
    reset_mask = None
    for line in lines:
        if line.startswith("mask"):
            mask = line.split(' = ')[1]
            reset_mask = int(mask.replace('1', '0').replace('X', '1'), 2)
            mask = int(mask.replace('X', '0'), 2)
        else:
            mem_string, number = line.split(' = ')
            print(number)
            print(reset_mask)
            number = (int(number) & reset_mask) | mask
            print(number)
            print()
            mem[mem_string[4:-1]] = number
    print(mem)
    print(sum(list(mem.values())))


def create_all_masks(mask):
    if mask.count('X') == 0:
        return [mask]
    else:
        all_masks = []
        index = mask.index('X')
        replacement_0 = mask[:index] + '0' + mask[index + 1:]
        all_masks += create_all_masks(replacement_0)
        replacement_1 = mask[:index] + '1' + mask[index + 1:]
        all_masks += create_all_masks(replacement_1)
        return all_masks

def solve2(file_name):
    lines = FileHandler(file_name).get_file_lines()
    mem = {}
    mask = None
    all_masks = None
    mask_original = None
    for line in lines:
        if line.startswith("mask"):
            mask_original = line.split(' = ')[1]
            mask = int(mask_original.replace('X', '0'), 2)
            all_masks = create_all_masks(mask_original.replace('1', '0'))
        else:
            mem_string, number = line.split(' = ')
            # just apply the 1 changes, don't take X into account
            mem_string = mem_string[4:-1]
            mem_string = (int(mem_string) | mask)
            # apply the X mask => 0 and 1 are enforced! => do same reset mask as in oef A
            for x_mask in all_masks:
                reset_mask = int(mask_original.replace('0', '1').replace('X', '0'), 2)
                mem_index = (mem_string & reset_mask) | int(x_mask, 2)
                mem[mem_index] = int(number)

    # print(mem)
    print(sum(list(mem.values())))
