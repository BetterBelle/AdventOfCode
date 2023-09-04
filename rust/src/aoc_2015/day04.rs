use std::fs;
use md5;

fn part1(input: &String) -> i32 {
    for i in 1..i32::MAX {
        let str: String = format!("{input}{i}");
        let digest: String = format!("{:x}", md5::compute(str.as_bytes()));

        if digest.starts_with("00000") {
            return i;
        }
    }
    return -1;
}

fn part2(input: &String) -> i32 {
    for i in 1..i32::MAX {
        let str: String = format!("{input}{i}");
        let digest: String = format!("{:x}", md5::compute(str.as_bytes()));

        if digest.starts_with("000000") {
            return i;
        }
    }
    return -1;
}

pub fn solve(filepath: &String) {
    let input: String = fs::read_to_string(filepath).unwrap();

    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}