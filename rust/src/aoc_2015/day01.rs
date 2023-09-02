use std::fs;

pub fn part1(input: &String) -> i32 {
    let mut floor: i32 = 0;
    for paren in input.chars() {
        match paren {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => ()
        }
    }

    return floor;
}

pub fn part2(input: &String) -> i32 {
    let mut floor: i32 = 0;
    for (i ,paren) in input.chars().enumerate() {
        match paren {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => ()
        } 
        if floor == -1 {
            return (i + 1).try_into().unwrap();
        }
    }

    return -1;
}

pub fn solve(filepath: &String) {
    let input: String = fs::read_to_string(filepath)
        .expect("Should have read the file.");

    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}