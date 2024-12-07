import os
from pprint import pprint

def coordinate_window_has_xmas_match(input_map, window):
    print("    ", window, end=" ")
    window_val = "".join([input_map[i][j] for (i, j) in window])
    print(window_val, window_val == "MAS", window_val == "SAM")
    return window_val == "MAS" or window_val == "SAM"

def check_diagonal_forward(input_map, i, j):
    n_rows = len(input_map)
    n_cols = len(input_map[0])

    inbound_horizontal_forward = j + 2 < n_cols
    inbound_vertical_forward = i + 2 < n_rows

    if inbound_horizontal_forward and inbound_vertical_forward:
        window = [(i + k, j + k) for k in range(3)]
        return coordinate_window_has_xmas_match(input_map, window)

    return False

def check_diagonal_backward(input_map, i, j):
    n_rows = len(input_map)
    n_cols = len(input_map[0])

    if i >= n_rows or j >= n_cols:
        return False

    inbound_horizontal_backward = j - 2 >= 0
    inbound_vertical_forward = i + 2 < n_rows

    print(i, j, n_rows, n_cols)
    if inbound_horizontal_backward and inbound_vertical_forward:
        window = [(i + k, j - k) for k in range(3)]
        return coordinate_window_has_xmas_match(input_map, window)
    return False

def has_xmas_match(input_map, i, j):
    print((i, j))

    coordinate_windows = []
    matches_diagonal_forward = check_diagonal_forward(input_map, i, j)
    matches_diagonal_backward = check_diagonal_backward(input_map, i, j + 2)
    return matches_diagonal_forward and matches_diagonal_backward

    print("  windows: ", end="")
    pprint(coordinate_windows)

    matching_windows = set([frozenset(window) for window in coordinate_windows if coordinate_window_has_xmas_match(input_map, window)])

    return matching_windows

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, "input/real.txt")
with open(file_path) as f:
    input_text = f.read()

input_map = input_text.strip().split("\n")

n_rows = len(input_map)
n_cols = len(input_map[0])

matches = set([])
n_matches = 0
for i in range(n_rows):
    for j in range(n_cols):
        matching_coordinate_windows = has_xmas_match(input_map, i, j)
        if matching_coordinate_windows:
            print("  ", i, j)
            n_matches += 1
        # for window in matching_coordinate_windows:
        #     if frozenset(window) not in matches:
        #         print("  ", i, j, window)
        #         n_matches += 1
        #         matches.add(window)

print("number of distinct matches:", n_matches)
# has_xmas_match(input_map, 4, 6)
# print()
# has_xmas_match(input_map, 0, 0)
# print()
# has_xmas_match(input_map, 0, 2)
