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

# 315048901   10.357    0.000   10.357    0.000 {built-in method builtins.len}

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


def get_file_window(diskmap_verbose, i_end):
    file_id = diskmap_verbose[i_end]

    i_begin_file = i_end
    while diskmap_verbose[i_begin_file - 1] == file_id:
        i_begin_file -= 1

    return (i_begin_file, i_end)

def find_next_free_space(i, diskmap_verbose):
    l = len(diskmap_verbose)

    return i


def move(diskmap_verbose, file_bounds):
    (i_begin_file, i_end_file) = file_bounds

    file_size = i_end_file - i_begin_file + 1
    diskmap_len = len(diskmap_verbose)

    i = 0
    moved = False
    while i < i_begin_file and not moved: 
        # print(f"    before = {i}; {diskmap_verbose[i:]}")
        # print(f"    before = {i}")

        # i_first_free_space = i + diskmap_verbose[i:].index(".")
        # i_first_free_space = find_next_free_space(i, diskmap_verbose)
        i_first_free_space = i + 1
        while diskmap_verbose[i_first_free_space] != ".":
            # print("oi")
            if i_first_free_space == diskmap_len - 1:
                break
            i_first_free_space += 1

        i_end_free_space_window_from_begin = i_first_free_space
        while i + i <= diskmap_len and diskmap_verbose[i_end_free_space_window_from_begin + 1] == ".":
            i_end_free_space_window_from_begin += 1
        # print(f"   {i}, ({i_begin_file}, {i_end_file}), ({i_first_free_space}, {i_end_free_space_window_from_begin})")
        # input()

        window_size = i_end_free_space_window_from_begin - i_first_free_space + 1

        if window_size >= file_size:
            # print("        will break!!")
            # move file
            moved = True
            file_id = diskmap_verbose[i_begin_file]
            diskmap_verbose[i_first_free_space: i_first_free_space + file_size] = [file_id] * file_size
            diskmap_verbose[i_begin_file: i_end_file + 1] = ["."] * file_size
            break

        i = i_end_free_space_window_from_begin + 1


def move_blocks(diskmap_verbose):
    i_end = len(diskmap_verbose) - 1
    while True:

        i_first_free_space = diskmap_verbose.index(".")
        # print(i_end, i_first_free_space)
        # print(i_end, i_first_free_space, "".join(diskmap_verbose))

        (i_begin_file, i_end_file) = get_file_window(diskmap_verbose, i_end)

        if i_end % 200 == 0:
            print(i_first_free_space, (i_begin_file, i_end_file))
            print(i_end)

        # print(i_first_free_space, (i_begin_file, i_end_file))

        if i_begin_file < i_first_free_space:
            break

        move(diskmap_verbose, (i_begin_file, i_end_file))
        i_end = i_begin_file - 1
    

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


