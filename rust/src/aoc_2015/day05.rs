use std::fs;
use regex;
use fancy_regex;

fn part1(input: &String) -> i32 {
    let find_vowels: regex::Regex = regex::Regex::new(r"a|e|i|o|u").unwrap();
    let find_doubles: fancy_regex::Regex = fancy_regex::Regex::new(r"(.)\1").unwrap();
    let find_invalid: regex::Regex = regex::Regex::new(r"ab|cd|pq|xy").unwrap();
    let mut nice: i32 = 0;

    for name in input.lines() {
        let invalid_count: i32 = find_invalid.find_iter(name).count() as i32;
        let vowel_count: i32 = find_vowels.find_iter(name).count() as i32;
        let doubles_count: i32 = find_doubles.find_iter(name).count() as i32;
        if vowel_count >= 3 && doubles_count >= 1 && invalid_count == 0 {
            nice += 1;
        }
    }
    return nice;
}

fn part2(input: &String) -> i32 {
    let find_squish: fancy_regex::Regex = fancy_regex::Regex::new(r"(.)(?!\1).\1").unwrap();
    let find_distinct_repeated_pair: fancy_regex::Regex = fancy_regex::Regex::new(r"(..).*\1").unwrap();
    let mut nice = 0;

    for name in input.lines() {
        let squished_count: i32 = find_squish.find_iter(name).count() as i32;
        let distinct_repeated_pair_count: i32 = find_distinct_repeated_pair.find_iter(name).count() as i32;
        if squished_count >= 1 && distinct_repeated_pair_count >= 1 {
            nice += 1;
        }
    }

    return nice;
}

pub fn solve(filepath: &String) {
    let input: String = fs::read_to_string(filepath).unwrap();

    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}