use clap::{Parser, Subcommand};
use std::error::Error;

mod days;
mod utils;

#[derive(Parser)]
#[command(version)]
struct Cli {
    #[command(subcommand)]
    command: Option<Commands>,
}

#[derive(Subcommand)]
enum Commands {
    /// Adds favorite command
    Run {
        #[arg(short, long)]
        challenge_id: String,
    },
}

// TODO -> should this not return a std::io::Error?
fn load_challenge(challenge_id: String) -> Result<(), Box<dyn Error>> {
    match challenge_id.as_str() {
        // day 1
        "1a" => Ok(days::day1::a::solve()?),
        "1b" => Ok(days::day1::b::solve()?),
        // day 2
        "2a" => Ok(days::day2::a::solve()?),
        "2b" => Ok(days::day2::b::solve()?),
        // day 3
        "3a" => Ok(days::day3::a::solve()?),
        "3b" => Ok(days::day3::b::solve()?),
        // day 4
        "4a" => Ok(days::day4::a::solve()?),
        "4b" => Ok(days::day4::b::solve()?),
        challenge_id_str => {
            Err(format!("Challenge {} invalid or not implemented!", challenge_id_str).into())
        }
    }
}

fn main() -> Result<(), Box<dyn Error>> {
    let cli = Cli::parse();

    match cli.command {
        Some(Commands::Run { challenge_id }) => {
            // println!("challenge_id {}", challenge_id);
            Ok(match load_challenge(challenge_id) {
                Err(err_str) => println!("{}", err_str),
                _ => (),
            })
        }
        None => panic!("Shouldn't happen"),
    }
}
