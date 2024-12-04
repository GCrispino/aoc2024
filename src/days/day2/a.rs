use std::error::Error;

use crate::utils;

use crate::days::day2::common::is_safe;

pub fn solve() -> Result<(), Box<dyn Error>> {
    let parsed = utils::read_from_file_to_number_matrix("day2/input/real.txt".to_string())?;

    let n_safe: i32 = parsed
        .iter()
        .map(is_safe)
        .map(|x| if x == true { 1 } else { 0 })
        .sum();

    println!("{}", n_safe);
    Ok(())
}
