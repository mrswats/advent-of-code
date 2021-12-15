use std::fs;
const BYTE_LENGTH: usize = 12;

fn main() {
    let filename = "src/day_3/input.txt";
    part1(filename);
    part2(filename);
}

fn part1(filename: &str) {
    let content = fs::read_to_string(filename).expect("Could not read the file :(");
    let mut report = vec![String::new(); BYTE_LENGTH];

    for line in content.split("\n") {
        if line == "" {
            continue;
        }

        for (i, c) in line.chars().enumerate() {
            report[i].push_str(&c.to_string());
        }
    }

    let mut gamma_rate = String::new();
    let mut epsilon_rate = String::new();

    for i in 0..BYTE_LENGTH {
        let number_of_ones = report[i].matches('1').count();
        let number_of_zeros = report[i].matches('0').count();
        gamma_rate.push_str(
            &{
                if number_of_ones > number_of_zeros {
                    '1'
                } else {
                    '0'
                }
            }
            .to_string(),
        );
        epsilon_rate.push_str(
            &{
                if number_of_ones < number_of_zeros {
                    '1'
                } else {
                    '0'
                }
            }
            .to_string(),
        )
    }

    let gamma_rate_dec = i64::from_str_radix(&gamma_rate, 2).unwrap();
    let epsilon_rate_dec = i64::from_str_radix(&epsilon_rate, 2).unwrap();

    println!("Gamma rate: {gamma_rate}, Epsilon rate: {epsilon_rate}");
    println!(
        "Gamma rate: {gamma_rate_dec}, Epsilon rate: {epsilon_rate_dec}\nTotal power: {}",
        gamma_rate_dec * epsilon_rate_dec,
    );
}

fn part2(filename: &str) {
    let content = fs::read_to_string(filename).expect("Could not read the file :(");
    let mut report = vec![String::new(); BYTE_LENGTH];

    for line in content.split("\n") {
        if line == "" {
            continue;
        }

        for (i, c) in line.chars().enumerate() {
            report[i].push_str(&c.to_string());
        }
    }

    let mut O2_gen = String::new();
    let mut CO2_gen = String::new();

    let mut O2_gen_rate = String::new();
    let mut CO2_gen_rate = String::new();

    for i in 0..BYTE_LENGTH {
        let number_of_ones = report[i].matches('1').count();
        let number_of_zeros = report[i].matches('0').count();
        O2_gen.push_str(
            &{
                if number_of_ones > number_of_zeros {
                    '1'
                } else {
                    '0'
                }
            }
            .to_string(),
        );

        let code_in_report = report.map(|x| {
            if x.starts_with(O2_gen) {
                return x;
            }
        });

        if code_in_report.len() == 1 {
            O2_gen_rate = code_in_report.pop()
        }

        CO2_gen.push_str(
            &{
                if number_of_ones < number_of_zeros {
                    '1'
                } else {
                    '0'
                }
            }
            .to_string(),
        );
    }

    let O2_gen_rate_dec = i64::from_str_radix(&O2_gen_rate, 2).unwrap();
    let CO2_gen_rate_dec = i64::from_str_radix(&CO2_gen_rate, 2).unwrap();

    println!("Oxygen Generation rate: {O2_gen_rate_dec}, CO2 Generation rate: {CO2_gen_rate_dec}");
    println!(
        "Life support rating: {}",
        O2_gen_rate_dec * CO2_gen_rate_dec
    );
}
