use std::fs;
use std::str::FromStr;

#[derive(Debug)]
enum Direction {
    Forward,
    Up,
    Down,
}

impl FromStr for Direction {
    type Err = ();

    fn from_str(input: &str) -> Result<Direction, Self::Err> {
        match input {
            "forward" => Ok(Direction::Forward),
            "up" => Ok(Direction::Up),
            "down" => Ok(Direction::Down),
            _ => Err(()),
        }
    }
}

#[derive(Debug)]
struct Instruction {
    direction: Direction,
    dist: i64,
}

fn main() {
    let filename = "./src/day_2/input_day_2.txt";
    println!("Day 2:");
    part1(filename);
    print!("\n");
    part2(filename);
}

fn part1(filename: &str) {
    println!("part 1");
    let content = fs::read_to_string(filename).expect("Could not read the file :(");

    let mut horizontal: i64 = 0;
    let mut vertical: i64 = 0;

    for line in content.split("\n") {
        if line == "" {
            continue;
        }
        let parsed = line.splitn(2, " ").collect::<Vec<&str>>();

        let inst = Instruction {
            direction: Direction::from_str(parsed[0]).unwrap(),
            dist: parsed[1].parse().unwrap(),
        };

        match inst.direction {
            Direction::Forward => horizontal += inst.dist,
            Direction::Up => vertical -= inst.dist,
            Direction::Down => vertical += inst.dist,
        }
    }

    println!("Horizontal: {}, Vertical: {}", horizontal, vertical);
    println!("{}", horizontal * vertical);
}

fn part2(filename: &str) {
    println!("part 2");
    let content = fs::read_to_string(filename).expect("Could not read the file :(");

    let mut horizontal: i64 = 0;
    let mut depth: i64 = 0;
    let mut aim: i64 = 0;

    for line in content.split("\n") {
        if line == "" {
            continue;
        }
        let parsed = line.splitn(2, " ").collect::<Vec<&str>>();

        let inst = Instruction {
            direction: Direction::from_str(parsed[0]).unwrap(),
            dist: parsed[1].parse().unwrap(),
        };

        match inst.direction {
            Direction::Forward => {
                horizontal += inst.dist;
                depth += aim * inst.dist;
            }
            Direction::Down => {
                aim += inst.dist;
            }
            Direction::Up => {
                aim -= inst.dist;
            }
        }
    }

    println!("Horizontal: {}, Depth: {}, Aim: {}", horizontal, depth, aim);
    println!("{}", horizontal * depth);
}
