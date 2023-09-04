use std::fs;

fn part1(floor_diffs: &Vec<i32>) -> i32 {
    let floor: i32 = floor_diffs.iter().sum();
    return floor;
}

fn part2(floor_diffs: &Vec<i32>) -> i32 {
    let floors_cumulative: Vec<i32> = floor_diffs.iter().scan(0, |acc: &mut i32, x: &i32| { *acc += x; Some(*acc) }).collect();
    let step_in_basement: i32 = floors_cumulative.iter().position(|x: &i32| *x == -1).unwrap() as i32;
    
    return step_in_basement + 1;
}

pub fn solve(filepath: &String) {
    let input: String = fs::read_to_string(filepath).unwrap();

    let floor_diffs: Vec<i32> = input.chars().into_iter().map(|x: char| if x == '(' { 1 } else { -1 }).collect();
    println!("Part 1: {}", part1(&floor_diffs));
    println!("Part 2: {}", part2(&floor_diffs));
}