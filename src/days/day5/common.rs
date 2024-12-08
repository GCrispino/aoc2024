use std::collections::{BTreeMap, HashSet, LinkedList};
use std::error::Error;
use std::fmt::Debug;

use crate::utils;

pub fn read_sections_from_file(
    input_file_path: String,
) -> Result<(Vec<String>, Vec<String>), Box<dyn Error>> {
    let input_str = utils::read_from_file_to_string(input_file_path)?;

    let parts: Vec<&str> = input_str.split("\n\n").collect();
    if parts.len() != 2 {
        return Err("length should be 2".into());
    }

    let first_section_str: Vec<String> = parts[0].lines().map(|s| s.to_string()).collect();
    let second_section_str: Vec<String> = parts[1].lines().map(|s| s.to_string()).collect();

    Ok((first_section_str, second_section_str))
}

pub fn is_update_ordered(rules_map: &BTreeMap<i32, LinkedList<Rule>>, update: &Vec<i32>) -> bool {
    let update_set: HashSet<&i32> = update.iter().collect();
    let mut processed_items: HashSet<i32> = HashSet::new();

    for page_number in update {
        // println!(
        //     "      page_number: {}, processed items: {:?}",
        //     page_number, processed_items
        // );
        let rule_list_opt = rules_map.get(page_number);
        if rule_list_opt.is_none() {
            processed_items.insert(*page_number);
            continue;
        }

        let rule_list = rule_list_opt.unwrap();

        // for rule_list in rules_map.values() {
        // println!("        rule_list: {:?}", rule_list);
        for rule in rule_list {
            if update_set.contains(&rule.0) && !processed_items.contains(&rule.0) {
                // println!(
                //     "        number {} should have already been processed!",
                //     rule.0
                // );
                return false;
            }
        }
        // }

        processed_items.insert(*page_number);
    }

    true
}

#[derive(Debug, PartialEq, PartialOrd)]
pub struct Rule(pub i32, pub i32);

impl From<&String> for Rule {
    fn from(value: &String) -> Self {
        value
            .find("|")
            .map(|i| {
                let first_num = &value[0..i].parse::<i32>().unwrap();
                let second_num = &value[i + 1..].parse::<i32>().unwrap();

                Rule(*first_num, *second_num)
            })
            .unwrap()
    }
}
