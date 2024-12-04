import math
import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, "input/real.txt")
with open(file_path) as f:
    seq = f.read()

def solve(seq):
    matches = list(re.finditer(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", seq))
    do_matches = list(re.finditer(r"do\(\)", seq))
    dont_matches = list(re.finditer(r"don't\(\)", seq))

    all_matches = sorted(matches + do_matches + dont_matches, key=lambda m: m.span())

    res = 0
    do = True
    for m in all_matches:
        matched_text = m.group()
        if matched_text == "do()":
            do = True
        if matched_text == "don't()":
            do = False

        if matched_text.startswith("mul") and do:
            res += math.prod(map(int, m.groups()))


    return res

print(solve(seq))
