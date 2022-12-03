use std::fs;

fn part1(filename: &str) {
    let mut prev: i64 = -1;
    let mut depth: i64;
    let mut count = 0;

    let content = fs::read_to_string(filename).expect("Could not read the file :(");

    for line in content.split('\n') {
        if line == "" {
            continue;
        }
        depth = line.parse::<i64>().unwrap();
        if prev != -1 && depth > prev {
            count += 1;
        }
        prev = depth;
    }

    println!("Depth: {}", count);
}

fn part2(filename: &str) {
    let mut prev: (i64, i64, i64) = (-1, -1, -1);
    let mut count = 0;

    let content = fs::read_to_string(filename).expect("Could not read the file :(");

    for line in content.split('\n') {
        if line == "" {
            continue;
        }

        let depth = line.parse::<i64>().unwrap();
        let prevs = prev.0 + prev.1 + prev.2;
        let currs = prev.1 + prev.2 + depth;

        if prev.0 != -1 && prev.1 != -1 && prev.2 != -1 && prevs < currs {
            count += 1;
        }

        prev.0 = prev.1;
        prev.1 = prev.2;
        prev.2 = depth;
    }

    println!("Depth: {}", count);
}

fn main() {
    println!("Day 1:");
    let filename = "./src/day_1/input_day_1.txt";
    part1(filename);
    part2(filename);
}
