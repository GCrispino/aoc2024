import math
import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, "input/real.txt")
with open(file_path) as f:
    seq = f.read()

def solve(seq):
    matches = re.finditer(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", seq)
    s = [math.prod(map(int, m.groups())) for m in matches]

    return sum(s)

print(solve(seq))
