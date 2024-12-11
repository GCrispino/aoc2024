import math
import os

from pprint import pprint


def get_input():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "input/real.txt")
    
    with open(file_path) as f:
        return list(map(int, f.read().strip().split(" ")))

def apply_blink_stone(stone):
    if stone == 0:
        return [1]

    n_digits = int(math.log10(stone)) + 1
    # print("  ", stone, n_digits, n_digits % 2 == 0)
    if n_digits % 2 != 0:
        # odd
        return [stone * 2024]

    # even
    n_digits_half = n_digits / 2
    ten_to_power = 10 ** n_digits_half

    first_half = int(stone // ten_to_power)
    second_half = int(stone % ten_to_power)

    return [first_half, second_half]


def apply_blink(stone_list):
    new_list = []
    for stone in stone_list:
        res_blink = apply_blink_stone(stone)
        new_list.extend(res_blink)

    return new_list


def solve(stone_list):
    # print(input_data)

    # print(problem_data)

    new_stone_list = stone_list
    for i in range(25):
        # print(i + 1, len(new_stone_list))
        # print(new_stone_list)

        new_stone_list = apply_blink(new_stone_list)

    # print(new_stone_list)

    res = len(new_stone_list)
    print(res)

    # pprint(antinodes)

input_data = get_input()
solve(input_data)


