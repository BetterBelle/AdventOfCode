use std::fs;
use std::collections::HashMap;

fn combinations(list: &Vec<i32>) -> Vec<Vec<i32>> {
    if list.len() == 0 {
        return vec![vec![]];
    }
    let mut cs = Vec::new();
    for val in combinations(&list[1..list.len()].to_vec()) {
        let mut other = val.clone();
        other.push(list[0]);
        cs.push(other);
        cs.push(val);
    }

    return cs;
}

fn create_numbers(input : &String) -> Vec<i32> {
    return input.lines().into_iter().map(|s| s.parse::<i32>().unwrap()).collect();
}

fn part1(nums : &Vec<i32>) -> i32 {
    let mut num_combinations = 0;
    for combination in combinations(&nums) {
        if combination.iter().fold(0, |acc, x| acc + x) == 150 {
            num_combinations += 1;
        }
    }

    return num_combinations;
}

fn part2(nums : &Vec<i32>) -> i32 {
    let mut totals : HashMap<usize, i32> = HashMap::new();
    for combination in combinations(&nums) {
        if combination.iter().fold(0, |acc, x| acc + x) == 150 {
            if !totals.contains_key(&combination.len()) {
                totals.insert(combination.len(), 1);
            }
            else {
                *totals.get_mut(&combination.len()).unwrap() += 1;
            }
        }
    }

    let min_key = totals.keys().min().unwrap();
    return *totals.get(min_key).unwrap();
}

pub fn solve(filepath: &String) {
    let input: String = fs::read_to_string(filepath).unwrap();
    let numbers = create_numbers(&input);

    println!("Part 1: {}", part1(&numbers));
    println!("Part 2: {}", part2(&numbers));
}
