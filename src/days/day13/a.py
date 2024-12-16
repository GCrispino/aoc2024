import math
import os

from pprint import pprint

from pulp import *

def define_prob(i, x1, x2, prize_x, y1, y2, prize_y):

    prob = LpProblem(f"machine_{i}", LpMinimize)


    a = LpVariable("a", 0, 100, "Integer")
    b = LpVariable("b", 0, 100, "Integer")

    prob += 3 * a + b, "obj"

    prob += x1*a + x2*b == prize_x, "c1"
    prob += y1*a + y2*b == prize_y, "c2"

    return prob

def parse_button_line(btn_info: str, btn_id: str):
    btn_stripped = btn_info.strip(f"Button {btn_id}: ")
    comma_spl = btn_stripped.split(", ")
    x = int(comma_spl[0].strip("X+"))
    y = int(comma_spl[1].strip("Y+"))

    return x, y

def parse_prize_line(prize_info: str):
    btn_stripped = prize_info.strip(f"Prize: ")
    comma_spl = btn_stripped.split(", ")
    x = int(comma_spl[0].strip("X="))
    y = int(comma_spl[1].strip("Y="))

    return x, y

def parse_machine_info(machine_info_lines):
    btn_a_info, btn_b_info, prize_info = machine_info_lines[:3]
    print("info:", btn_a_info, btn_b_info, prize_info)

    x1, y1 = parse_button_line(btn_a_info, "A")
    x2, y2 = parse_button_line(btn_b_info, "B")

    prize_x, prize_y = parse_prize_line(prize_info)

    print(x1, y1, x2, y2, prize_x, prize_y)
    return x1, y1, x2, y2, prize_x, prize_y

def get_input():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "input/real.txt")
    
    with open(file_path) as f:
        machines_info = [x for x in f.read().strip().split("\n\n")]
        return [parse_machine_info(machine_info.split("\n")) for machine_info in machines_info]

def solve(machines_info):
    n_tokens = 0
    probs = []
    for i, m in enumerate(machines_info):
        x1, y1, x2, y2, prize_x, prize_y = m
        prob = define_prob(i, x1, x2, prize_x, y1, y2, prize_y)
        prob.solve(PULP_CBC_CMD(msg=False))
        probs.append(prob)
        v = value(prob.objective)
        if prob.status == 1:
            n_tokens += v
        # print(prob)
        # print(f"obj for prob {i}: {v}. total = {n_tokens}")
        # print()

    # print(input_data)

    print()
    print(n_tokens)

input_data = get_input()
solve(input_data)


