use std::fs;
use num::complex;
use std::collections::HashSet;

fn part1(input: &String) -> i32 {
    let mut position: complex::Complex<i32> = complex::Complex::new(0, 0);
    let mut dict: HashSet<complex::Complex<i32>> = HashSet::new();
    // Insert the starting gift at position 0
    dict.insert(position);
    
    for direction in input.chars() {
        match direction {
            '>' => position.re += 1,
            '<' => position.re -= 1,
            '^' => position.im += 1,
            'v' => position.im -= 1,
            _ => ()
        }
        dict.insert(position);
    }

    return dict.len() as i32;
}


fn part2(input: &String) -> i32 {
    let mut santa: complex::Complex<i32> = complex::Complex::new(0, 0);
    let mut robo_santa: complex::Complex<i32> = complex::Complex::new(0, 0);
    let mut dict: HashSet<complex::Complex<i32>> = HashSet::new();

    // Insert the starting 2 gifts at position 0
    dict.insert(santa);

    for (i, direction) in input.chars().enumerate() {
        let position: &mut num::Complex<i32> = if i % 2 == 0 { &mut santa } else { &mut robo_santa };
        match direction {
            '>' => position.re += 1,
            '<' => position.re -= 1,
            '^' => position.im += 1,
            'v' => position.im -= 1,
            _ => ()
        }
        dict.insert(*position);
    }
    return dict.len() as i32;
}

pub fn solve(filepath: &String) {
    let input: String = fs::read_to_string(filepath).unwrap();

    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}