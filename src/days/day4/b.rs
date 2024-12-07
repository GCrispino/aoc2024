use std::error::Error;

use crate::utils;

pub fn solve() -> Result<(), Box<dyn Error>> {
    let input_map = utils::read_from_file_to_string_list("day4/input/real.txt".to_string())?;

    let n_rows = input_map.len() as isize;
    let n_cols = input_map[0].len() as isize;

    let mut n_matches = 0;
    for i in 0..n_rows {
        for j in 0..n_cols {
            let matches = has_xmas_match(&input_map, i, j);

            if matches {
                n_matches += 1;
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

    return window_val == "MAS" || window_val == "SAM";
}

fn check_diagonal_forward(input_map: &Vec<String>, i: isize, j: isize) -> bool {
    let n_rows = input_map.len() as isize;
    let n_cols = input_map[0].len() as isize;

    let inbound_horizontal_forward = j + 2 < n_cols;
    let inbound_vertical_forward = i + 2 < n_rows;

    if inbound_horizontal_forward && inbound_vertical_forward {
        let window: Vec<(isize, isize)> = (0..3).map(|k| (i + k, j + k)).collect();
        return coordinate_window_has_xmas_match(input_map, &window);
    }

    false
}

fn check_diagonal_backward(input_map: &Vec<String>, i: isize, j: isize) -> bool {
    let n_rows = input_map.len() as isize;
    let n_cols = input_map[0].len() as isize;

    if i >= n_rows || j >= n_cols {
        return false;
    }

    let inbound_horizontal_backward = j - 2 >= 0;
    let inbound_vertical_forward = i + 2 < n_rows;

    if inbound_horizontal_backward && inbound_vertical_forward {
        let window: Vec<(isize, isize)> = (0..3).map(|k| (i + k, j - k)).collect();
        return coordinate_window_has_xmas_match(input_map, &window);
    }

    false
}

fn has_xmas_match(input_map: &Vec<String>, i: isize, j: isize) -> bool {
    let matches_diagonal_forward = check_diagonal_forward(input_map, i, j);
    let matches_diagonal_backward = check_diagonal_backward(input_map, i, j + 2);

    matches_diagonal_forward && matches_diagonal_backward
}
