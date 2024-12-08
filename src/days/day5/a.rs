use std::collections::{BTreeMap, LinkedList};
use std::convert::From;
use std::error::Error;

use crate::days::day5::common;
use crate::days::day5::common::{is_update_ordered, Rule};

pub fn solve() -> Result<(), Box<dyn Error>> {
    let (first_section_str, second_section_str) =
        common::read_sections_from_file("day5/input/real.txt".to_string())?;

    let mut rules: BTreeMap<i32, LinkedList<Rule>> = BTreeMap::new();

    first_section_str.iter().for_each(|rule_str| {
        let r = Rule::from(rule_str);

        // println!("RULE {:?}", r);
        rules
            .entry(r.1)
            .and_modify(|list| list.push_back(Rule(r.0, r.1)))
            .or_insert(LinkedList::from([r]));
        ()
    });

    let updates: Vec<Vec<i32>> = second_section_str
        .iter()
        .map(|page_str| {
            page_str
                .split(",")
                .map(|x| x.parse::<i32>().unwrap())
                .collect()
        })
        .collect();

    // println!("rules: {:?}", rules);
    // println!("updates: {:?}", updates);

    let res: i32 = updates
        .iter()
        .filter_map(|update| {
            // println!("  update: {:?}", update);

            if !is_update_ordered(&rules, update) {
                // println!("    unordered!");
                return None;
            }

            let n = update.len();
            let i_middle = n / 2;

            // println!("    ordered! middle: {}", update[i_middle]);
            Some(update[i_middle])
        })
        .sum();

    println!("{}", res);

    Ok(())
}
