use std::fs;
use num::complex;
use std::collections::HashMap;

pub fn part1(input: &String) -> i32 {
    let mut position: complex::Complex<i32> = complex::Complex::new(0, 0);
    let mut dict: HashMap<complex::Complex<i32>, i32> = HashMap::new();
    // Insert the starting gift at position 0
    dict.insert(position, 1);
    
    for direction in input.chars() {
        match direction {
            '>' => position.re += 1,
            '<' => position.re -= 1,
            '^' => position.im += 1,
            'v' => position.im -= 1,
            _ => ()
        }
        dict.entry(position).and_modify(|x: &mut i32| *x += 1).or_insert(1);
    }

    return dict.keys().len() as i32;
}


pub fn part2(input: &String) -> i32 {
    let mut santa: complex::Complex<i32> = complex::Complex::new(0, 0);
    let mut robo_santa: complex::Complex<i32> = complex::Complex::new(0, 0);
    let mut dict: HashMap<complex::Complex<i32>, i32> = HashMap::new();
    // Insert the starting 2 gifts at position 0
    dict.insert(santa, 2);
    let mut position: &mut complex::Complex<i32>;

    for (i, direction) in input.chars().enumerate() {
        if i % 2 == 0 {
            position = &mut santa;
        }
        else {
            position = &mut robo_santa;
        } 
        match direction {
            '>' => position.re += 1,
            '<' => position.re -= 1,
            '^' => position.im += 1,
            'v' => position.im -= 1,
            _ => ()
        }
        dict.entry(*position).and_modify(|x: &mut i32| *x += 1).or_insert(1);
    }
    return dict.keys().len() as i32;
}

pub fn solve(filepath: &String) {
    let input: String = fs::read_to_string(filepath)
        .expect("Should have read the file.");

    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}