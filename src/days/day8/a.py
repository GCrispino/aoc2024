import os
import numpy as np

from pprint import pprint


def get_input():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "input/real.txt")
    
    lines = []
    with open(file_path) as f:
        lines = [line.strip() for line in f.readlines()]

    n_rows = len(lines)
    n_cols = len(lines[0])

    problem_data = {
        "n_rows": n_rows,
        "n_cols": n_cols,
        "locations": {},
        "raw_lines": lines,
    }

    locations = problem_data["locations"]
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == ".":
                continue

            if c not in locations:
                locations[c] = []

            locations[c].append((i, j))

    return problem_data

def compute_antinode_loc_from_locs(loc1, loc2):
    loc1 = np.array(loc1)
    loc2 = np.array(loc2)

    diff_vector = loc1 - loc2

    return (
        tuple((loc1 + diff_vector)),
        tuple((loc2 - diff_vector))
    )

def find_antinodes(problem_data):
    locations = problem_data["locations"]
    antinode_locations = set()

    for _, freq_locations in locations.items():
        for i_location, freq_location in enumerate(freq_locations):
            for j_location, freq_location2 in enumerate(freq_locations):
                if i_location == j_location:
                    continue
                new_antinode_locations = compute_antinode_loc_from_locs(freq_location, freq_location2)

                for antinode_loc in new_antinode_locations:
                    in_bounds_i = antinode_loc[0] >= 0 and antinode_loc[0] < problem_data["n_rows"]
                    in_bounds_j = antinode_loc[1] >= 0 and antinode_loc[1] < problem_data["n_cols"]
                    if in_bounds_i and in_bounds_j:
                        antinode_locations.add(antinode_loc)


                # print(new_antinode_locations)
                # antinode_locations.extend(new_antinode_locations)
    return antinode_locations

def print_map_with_antinode_locations(problem_data, antinode_locations):
    lines = [list(l) for l in problem_data["raw_lines"]]

    for (i, j) in antinode_locations:
        lines[i][j] = "#"

    final_string = "\r\n".join(["".join(l) for l in lines])
    print(final_string)


def solve(problem_data):
    # print(input_data)

    # print(problem_data)

    antinode_locations = find_antinodes(problem_data)
    
    # print()
    # print_map_with_antinode_locations(problem_data, antinode_locations)
    # pprint(antinode_locations)

    res = len(antinode_locations)
    print(res)

    # pprint(antinodes)

input_data = get_input()
solve(input_data)


