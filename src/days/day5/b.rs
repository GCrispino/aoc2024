use std::collections::{HashSet, LinkedList};
use std::error::Error;

use crate::days::day5::common;
use crate::days::day5::common::Rule;

use crate::utils::types::graph::{noop_dfs, Graph};

pub fn solve() -> Result<(), Box<dyn Error>> {
    let (first_section_str, second_section_str) =
        common::read_sections_from_file("day5/input/real.txt".to_string())?;

    let rules: Vec<Rule> = first_section_str
        .iter()
        .map(|rule_str| {
            let r = Rule::from(rule_str);

            r
        })
        .collect();
    let mut rules_graph: Graph = rules.iter().map(|r| (r.0, r.1)).collect();

    rules.iter().for_each(|r| {
        if rules_graph.get_adj(r.1).is_none() {
            rules_graph.add_node(r.1);
        }
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

    let res: i32 = updates
        .iter()
        .filter_map(|update| {
            let ordered_update = get_ordered_update(update, &rules_graph);
            // println!("  update: {:?}", update);

            let n = std::cmp::min(update.len(), ordered_update.len());
            if update.iter().take(n).eq(ordered_update.iter().take(n)) {
                return None;
            }
            let n = ordered_update.len();
            let i_middle = n / 2;

            // let r = *ordered_update.iter().nth(i_middle).unwrap();
            // println!(
            //     "    now ordered! middle: {}, update: {:?}, r = {}",
            //     i_middle, ordered_update, r
            // );
            Some(*ordered_update.iter().nth(i_middle).unwrap())
        })
        .sum();

    println!("{}", res);

    Ok(())
}

fn get_ordered_update(update: &Vec<i32>, rules_graph: &Graph) -> LinkedList<i32> {
    // println!("{:?}", update);

    let mut stack = LinkedList::new();
    let mut visited: HashSet<i32> = HashSet::new();

    let sub_graph_keys: Vec<(i32, i32)> = update
        .iter()
        .flat_map(|node| {
            let adj_list = rules_graph.get_adj(*node).unwrap();

            let y = adj_list.iter().map(|adj| (*node, *adj));
            y
        })
        .collect();

    let sub_rules_graph: Graph = sub_graph_keys.iter().map(|x| *x).collect();
    for ele in update {
        if visited.contains(ele) {
            continue;
        }
        // println!(
        //     "Running DFS for {}, visited: {:?}, stack: {:?}",
        //     ele, visited, stack
        // );
        stack.extend(sub_rules_graph.dfs(*ele, &mut noop_dfs, Some(&mut visited)));
    }

    stack.iter().map(|x| *x).rev().collect()
}
