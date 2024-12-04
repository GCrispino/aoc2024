use regex::Regex;
use std::error::Error;

use crate::utils;

pub fn solve() -> Result<(), Box<dyn Error>> {
    let program = utils::read_from_file_to_string("day3/input/real.txt".to_string())?;

    let re = Regex::new(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)").unwrap();

    let matches: Result<Vec<_>, Box<dyn Error>> = re
        .captures_iter(&program)
        .map(|caps| {
            // println!("{}", &m[0]);
            let x = caps[1].parse::<i32>()?;
            let y = caps[2].parse::<i32>()?;

            Ok(x * y)
        })
        .collect();

    // println!("{:?}", matches);

    let res: i32 = matches?.into_iter().sum();

    println!("{}", res);

    Ok(())
}
