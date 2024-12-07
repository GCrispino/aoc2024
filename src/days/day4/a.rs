use std::collections::{BTreeSet, HashSet};
use std::error::Error;

use crate::utils;

pub fn solve() -> Result<(), Box<dyn Error>> {
    let input_map = utils::read_from_file_to_string_list("day4/input/real.txt".to_string())?;

    let n_rows = input_map.len() as isize;
    let n_cols = input_map[0].len() as isize;

    let mut matches: HashSet<Window> = HashSet::new();
    let mut n_matches = 0;

    for i in 0..n_rows {
        for j in 0..n_cols {
            let matching_coordinate_windows = has_xmas_match(&input_map, i, j);

            for window in matching_coordinate_windows {
                match matches.get(&window) {
                    None => {
                        n_matches += 1;
                        matches.insert(window);
                    }
                    Some(_) => (),
                }
            }
        }
    }

    println!("{}", n_matches);
    Ok(())
}

fn coordinate_window_has_xmas_match(input_map: &Vec<String>, window: &Vec<(isize, isize)>) -> bool {
    let window_val_vec: Vec<String> = window
        .iter()
        .map(|(i, j)| {
            let i_usize: usize = (*i).try_into().unwrap();
            let j_usize: usize = (*j).try_into().unwrap();
            let row = input_map[i_usize].clone();
            let char = row.chars().nth(j_usize);
            char.unwrap_or(0 as char).to_string()
        })
        .collect();

    let window_val = window_val_vec.join("");

    return window_val == "XMAS" || window_val == "SAMX";
}

type Window = BTreeSet<(isize, isize)>;

fn has_xmas_match(input_map: &Vec<String>, i: isize, j: isize) -> HashSet<Window> {
    let n_rows = input_map.len() as isize;
    let n_cols = input_map[0].len() as isize;

    // println!("{:?}", (i, j));

    let inbound_horizontal_forward = j + 3 < n_cols;
    let inbound_horizontal_backward = j - 3 >= 0;

    let inbound_vertical_forward = i + 3 < n_rows;
    let inbound_vertical_backward = i - 3 >= 0;

    let mut coordinate_windows: Vec<Vec<(isize, isize)>> = vec![];

    if inbound_horizontal_forward {
        coordinate_windows.push((0..4).map(|k| (i, j + k)).collect());
    }
    if inbound_horizontal_backward {
        coordinate_windows.push((0..4).map(|k| (i, j + k - 3)).collect());
    }

    if inbound_vertical_forward {
        coordinate_windows.push((0..4).map(|k| (i + k, j)).collect());
    }
    if inbound_vertical_backward {
        coordinate_windows.push((0..4).map(|k| (i + k - 3, j)).collect());
    }

    if inbound_horizontal_forward && inbound_vertical_forward {
        coordinate_windows.push((0..4).map(|k| (i + k, j + k)).collect());
    }
    if inbound_horizontal_backward && inbound_vertical_forward {
        coordinate_windows.push((0..4).map(|k| (i + k, j - k)).collect());
    }
    if inbound_horizontal_forward && inbound_vertical_backward {
        coordinate_windows.push((0..4).map(|k| (i - k, j + k)).collect());
    }
    if inbound_horizontal_backward && inbound_vertical_backward {
        coordinate_windows.push((0..4).map(|k| (i + k - 3, j + k - 3)).collect());
    }

    let matching_windows: HashSet<Window> = coordinate_windows
        .iter()
        .filter(|window_as_vec| coordinate_window_has_xmas_match(input_map, window_as_vec))
        .map(|window_as_vec| BTreeSet::from_iter(window_as_vec.iter().cloned()))
        .collect();

    matching_windows
}
