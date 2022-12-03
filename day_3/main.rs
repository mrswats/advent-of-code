use std::fs;
const BYTE_LENGTH: usize = 12;

fn main() {
    let filename = "src/day_3/input.txt";
    println!("Part1:");
    part1(filename);
    println!("\nPart2:");
    part2(filename);
}

fn part1(filename: &str) {
    let content = fs::read_to_string(filename).expect("Could not read the file :(");
    let mut report = vec![String::new(); BYTE_LENGTH];

    for line in content.lines() {
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
    let content =
        fs::read_to_string(filename).expect("Something went wrong when reading the file :/");
    let input = content.lines().collect::<Vec<&str>>();

    let mut o2_codes = input.clone();
    let mut o2_rating = String::new();
    let mut o2_gen_rating = "";

    let mut co2_codes = input.clone();
    let mut co2_rating = String::new();
    let mut co2_scrub_rating = "";

    for i in 0..BYTE_LENGTH {
        let mut o2_report = String::new();
        for code in &o2_codes {
            o2_report.push_str(&code.chars().nth(i).unwrap().to_string());
        }
        let number_of_ones = { o2_report.matches('1').count() };
        let number_of_zeros = { o2_report.matches('0').count() };

        o2_rating.push_str(
            &{
                if number_of_ones >= number_of_zeros {
                    '1'
                } else {
                    '0'
                }
            }
            .to_string(),
        );

        let mut temp_codes = Vec::<&str>::new();

        for code in &o2_codes {
            if code.starts_with(&o2_rating) {
                temp_codes.push(&code);
            };
        }
        o2_codes = temp_codes.clone();

        if o2_codes.len() == 1 && o2_gen_rating == "" {
            o2_gen_rating = o2_codes[0];
            break;
        }
    }

    for i in 0..BYTE_LENGTH {
        let mut co2_report = String::new();
        for code in &co2_codes {
            co2_report.push_str(&code.chars().nth(i).unwrap().to_string());
        }
        let number_of_ones = { co2_report.matches('1').count() };
        let number_of_zeros = { co2_report.matches('0').count() };

        co2_rating.push_str(
            &{
                if number_of_ones >= number_of_zeros {
                    '0'
                } else {
                    '1'
                }
            }
            .to_string(),
        );

        let mut temp_codes = Vec::<&str>::new();

        for code in &co2_codes {
            if code.starts_with(&co2_rating) {
                temp_codes.push(&code);
            };
        }
        co2_codes = temp_codes.clone();

        if co2_codes.len() == 1 && co2_scrub_rating == "" {
            co2_scrub_rating = co2_codes[0];
            break;
        }
    }

    let o2_generation_rate_decimal = i64::from_str_radix(&o2_gen_rating, 2).unwrap();
    let co2_scrubbing_rate_decimal = i64::from_str_radix(&co2_scrub_rating, 2).unwrap();

    println!("Oxygen Generation Ragin: {o2_generation_rate_decimal}, CO2 Scrubbing Rate: {co2_scrubbing_rate_decimal}");
    println!(
        "Life support rating: {}",
        o2_generation_rate_decimal * co2_scrubbing_rate_decimal
    );
}
