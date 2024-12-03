use std::error::Error;
use std::fs;

pub fn read_from_file_to_string(rel_path: String) -> Result<String, Box<dyn Error>> {
    let cur_dir_blah = std::env::current_dir()?;
    let cur_dir_opt = cur_dir_blah.to_str();

    let cur_dir_res: Result<&str, Box<dyn Error>> = match cur_dir_opt {
        Some(s) => Ok(s),
        None => Err("".into()),
    };

    let cur_dir = cur_dir_res?;

    let input_path = format!("{}/src/days/{}", cur_dir, rel_path);
    println!("{}", input_path.clone());

    let res = fs::read_to_string(input_path)?;

    Ok(res)
}

pub fn read_from_file_to_number_tuples(
    rel_path: String,
) -> Result<Vec<(i32, i32)>, Box<dyn Error>> {
    let file_contents = read_from_file_to_string(rel_path)?;
    let spl = file_contents.split("\n");
    let n = spl.clone().count();
    let parsed: Result<Vec<(i32, i32)>, Box<dyn Error>> = spl
        .take(n - 1)
        .map(|s| {
            let v: Vec<&str> = s.split_whitespace().collect();

            let x = v[0].parse::<i32>()?;
            let y = v[1].parse::<i32>()?;

            Ok((x, y))
        })
        .collect();

    parsed
}
