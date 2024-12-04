fn is_all_increasing(levels: &Vec<i32>) -> bool {
    for i in 1..levels.len() {
        let prev_val = levels[i - 1];
        let val = levels[i];

        if val <= prev_val {
            // println!("NOT INCREASING {:?}", levels);
            return false;
        }
    }

    true
}

fn is_all_decreasing(levels: &Vec<i32>) -> bool {
    for i in 1..levels.len() {
        let prev_val = levels[i - 1];
        let val = levels[i];

        if val >= prev_val {
            // println!("NOT DECREASING {:?}", levels);
            return false;
        }
    }

    true
}

pub fn is_safe(levels: &Vec<i32>) -> bool {
    if !is_all_increasing(&levels) && !is_all_decreasing(&levels) {
        // println!("NOT SAFE 1 {:?}", levels);
        return false;
    }

    for i in 1..levels.len() {
        let prev_val = levels[i - 1];
        let val = levels[i];

        let abs_diff = (val - prev_val).abs();
        if abs_diff < 1 || abs_diff > 3 {
            // println!("NOT SAFE 2 {:?}", levels);
            return false;
        }
    }

    // println!("SAFE {:?}", levels);
    true
}

pub fn is_safe_by_removing_level(levels: &Vec<i32>) -> bool {
    if is_safe(levels) {
        return true;
    }

    for i in 0..levels.len() {
        let with_removed: Vec<_> = levels[..i]
            .iter()
            .chain(&levels[i + 1..])
            .cloned()
            .collect();

        if is_safe(&with_removed) {
            return true;
        }
    }

    // println!("SAFE {:?}", levels);
    false
}
