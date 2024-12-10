import os
from math import log10
from pprint import pprint
from itertools import product


def parse_input_line(line):
    line = line.strip()
    spl = line.split(": ")
    calibration_res = int(spl[0])
    operands = list(map(int, spl[1].split()))

    return calibration_res, operands

    
def get_input():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "input/real.txt")
    with open(file_path) as f:
        return [parse_input_line(line) for line in f.readlines()]

def concat(x, y):
    n_digits = int(log10(y) + 1)
    return x * (10 ** n_digits) + y

op_map = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
    # "||": lambda x, y: int(str(x) + str(y)),
    "||": concat,
}

def eval(op, args):
    fn = op_map[op]
    return fn(*args)

def check_combination(op_combination, all_args, calibration_res):
    actual_res = all_args[0]
    for i in range(1, len(all_args)):
        args = (actual_res, all_args[i])
        op = op_combination[i - 1]
        actual_res = eval(op, args)
        if actual_res > calibration_res:
            return False

    return actual_res == calibration_res


def solve(input_data):
    operators = list(op_map.keys())
    truthy_equations = []
    n_equations = len(input_data)
    for i, (calibration_res, operands) in enumerate(input_data):
        if (i + 1) % 50 == 0:
            print(f"{i + 1}/{n_equations}")
        # print(f"equation: {(calibration_res, operands)}")
        n_eq_operators = len(operands) - 1
        operator_combinations = product(*([operators] * n_eq_operators))

        for op_combination in operator_combinations:
            valid_combination = check_combination(op_combination, operands, calibration_res)
            # print("  combination: ", op_combination, valid_combination)
            if valid_combination:
                truthy_equations.append(i)
                break

    res = sum([input_data[i][0] for i in truthy_equations])
    print(res)


input_data = get_input()
solve(input_data)


