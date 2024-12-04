use regex::{Captures, Regex};
use std::error::Error;

use crate::utils;

pub fn solve() -> Result<(), Box<dyn Error>> {
    let program = utils::read_from_file_to_string("day3/input/real.txt".to_string())?;

    let re_mul = Regex::new(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)").unwrap();
    let re_do = Regex::new(r"do\(\)").unwrap();
    let re_dont = Regex::new(r"don't\(\)").unwrap();

    let mul_matches: Vec<Captures> = re_mul.captures_iter(&program).collect();
    let do_matches: Vec<Captures> = re_do.captures_iter(&program).collect();
    let dont_matches: Vec<Captures> = re_dont.captures_iter(&program).collect();

    let mut all_matches: Vec<Captures> = vec![];
    all_matches.extend(mul_matches);
    all_matches.extend(do_matches);
    all_matches.extend(dont_matches);
    all_matches.sort_by_key(|m| {
        let y = m.get(0).unwrap();
        y.start()
    });

    let mut res = 0;
    let mut do_mul = true;
    for m in all_matches {
        let matched_text = m.get(0).unwrap().as_str();

        if matched_text == "do()" {
            do_mul = true;
        }
        if matched_text == "don't()" {
            do_mul = false;
        }

        if matched_text.starts_with("mul") && do_mul {
            let subcaps = m.iter().skip(1).map(|_m| {
                let m = _m.unwrap();
                // println!("{:?}, {}", m, m.as_str());
                let x = m.as_str().parse::<i32>().unwrap();
                x
            });

            // println!("ns: {:?}", subcaps.clone());
            let prod = subcaps.fold(1, |acc, x| acc * x);
            // println!("prod: {:?}", prod);
            res += prod;
        }
    }

    println!("{}", res);

    Ok(())
}
