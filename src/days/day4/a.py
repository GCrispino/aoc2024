import os
from pprint import pprint

def coordinate_window_has_xmas_match(input_map, window):
    window_val = "".join([input_map[i][j] for (i, j) in window])
    # print("    ", window_val, window_val == "XMAS", window_val == "SAMX")
    return window_val == "XMAS" or window_val == "SAMX"

def has_xmas_match(input_map, i, j):
    n_rows = len(input_map)
    n_cols = len(input_map[0])

    # print((i, j))

    inbound_horizontal_forward = j + 3 < n_cols
    inbound_horizontal_backward = j - 3 >= 0

    inbound_vertical_forward = i + 3 < n_rows
    inbound_vertical_backward = i - 3 >= 0
    # print(
    #         inbound_horizontal_forward,
    #         inbound_horizontal_backward,
    #         inbound_vertical_forward,
    #         inbound_vertical_backward,
    # )

    coordinate_windows = []
    if inbound_horizontal_forward:
        coordinate_windows.append([(i, j + k) for k in range(4)])
    if inbound_horizontal_backward:
        coordinate_windows.append([(i, j + k) for k in range(-3, 1)])

    if inbound_vertical_forward:
        coordinate_windows.append([(i + k, j) for k in range(4)])
    if inbound_vertical_backward:
        coordinate_windows.append([(i + k, j) for k in range(-3, 1)])

    if inbound_horizontal_forward and inbound_vertical_forward:
        coordinate_windows.append([(i + k, j + k) for k in range(4)])
    if inbound_horizontal_backward and inbound_vertical_forward:
        # coordinate_windows.append(frozenset([(i + k, j + l) for k in range(-3, 1) for l in range(4)]))
        coordinate_windows.append([(i + k, j - k) for k in range(4)])
    if inbound_horizontal_forward and inbound_vertical_backward:
        # coordinate_windows.append(frozenset([(i + k, j + l) for k in range(4) for l in range(-3, 1)]))
        coordinate_windows.append([(i - k, j + k) for k in range(4)])
    if inbound_horizontal_backward and inbound_vertical_backward:
        coordinate_windows.append([(i + k, j + k) for k in range(-3, 1)])

    # print("windows: ", end="")
    # pprint(coordinate_windows)

    matching_windows = set([frozenset(window) for window in coordinate_windows if coordinate_window_has_xmas_match(input_map, window)])

    return matching_windows

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, "input/real.txt")
with open(file_path) as f:
    input_text = f.read()

# input_text = """MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# """

input_map = input_text.strip().split("\n")
# pprint(input_map)

# matching_coordinate_windows = has_xmas_match(input_map, 0, 4)
# exit(0)

n_rows = len(input_map)
n_cols = len(input_map[0])

matches = set([])
n_matches = 0
for i in range(n_rows):
    for j in range(n_cols):
        matching_coordinate_windows = has_xmas_match(input_map, i, j)
        for window in matching_coordinate_windows:
            if window not in matches:
                # print("  ", i, j, window)
                n_matches += 1
                matches.add(window)

print("number of distinct matches:", n_matches)
# has_xmas_match(input_map, 4, 6)
# print()
# has_xmas_match(input_map, 0, 0)
# print()
# has_xmas_match(input_map, 0, 2)
