import os
from pprint import pprint
from itertools import product


def get_input():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "input/real.txt")
    with open(file_path) as f:
        return f.read().strip()

def parse_diskmap_verbose(diskmap):
    char_type_file = True
    diskmap_verbose_str_list = []
    for id, c in enumerate(diskmap):
        id = id // 2
        # print(diskmap_verbose_str_list)
        c = int(c)
        if char_type_file:
            diskmap_verbose_str_list.extend([str(id)] * c)
        else:
            diskmap_verbose_str_list.extend(["."] * c)

        char_type_file = not char_type_file
        
    return diskmap_verbose_str_list

def get_n_free_space_end(diskmap_verbose):
    n = 0
    for i in range(len(diskmap_verbose) - 1, -1, -1):
        if diskmap_verbose[i] != ".":
            break
        n += 1

    return n

def get_i_first_trailing_free_space(diskmap_verbose):
    i = None
    # for _i, c in enumerate(reversed(diskmap_verbose)):
    for _i in range(len(diskmap_verbose) - 1, -1, -1):
        c = diskmap_verbose[_i]
        # print("    ", _i, c)
        if c != ".":
            break
        i = _i
        # i = len(diskmap_verbose) - 1 - _i

    return i



def move(diskmap_verbose, i_first_free_space, i_end):
    last_char = diskmap_verbose[i_end]
    diskmap_verbose[i_first_free_space] = last_char
    diskmap_verbose[i_end] = "."


def move_blocks(diskmap_verbose):
    i_end = len(diskmap_verbose) - 1
    while True:
        # print(i_end, "".join(diskmap_verbose))

        i_first_free_space = diskmap_verbose.index(".")
        i_first_trailing_free_space = get_i_first_trailing_free_space(diskmap_verbose)

        # if i_end % 5000 == 0:
        #     print(i_first_free_space, i_first_trailing_free_space)
        #     print(i_end)

        if i_first_free_space == i_first_trailing_free_space:
            break

        # n_free_space = len([c for c in diskmap_verbose if c == "."]) 
        # n_free_space_end = get_n_free_space_end(diskmap_verbose)
        #
        # if n_free_space == n_free_space_end:
        #     break

        move(diskmap_verbose, i_first_free_space, i_end)
        i_end -= 1
    

    return diskmap_verbose


def solve(input_data):
    # print(input_data)

    diskmap_verbose = parse_diskmap_verbose(input_data)

    # print("".join(diskmap_verbose))

    move_blocks(diskmap_verbose)

    # print("".join(diskmap_verbose))
    res = sum([i * int(c) if c != "." else 0 for i, c in enumerate(diskmap_verbose)])

    print(res)


input_data = get_input()
solve(input_data)


