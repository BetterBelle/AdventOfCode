use std::fs;
use regex;

fn part1(input: &String) -> i32 {
    let mut grid: [[i32; 1000]; 1000] = [[0; 1000]; 1000];
    let coord_capture: regex::Regex = regex::Regex::new(r"[0-9]*,[0-9]*").unwrap();
    let word_matcher: regex::Regex = regex::Regex::new(r"toggle|off|on").unwrap();

    for line in input.lines() {
        let matches: Vec<regex::Match<'_>> = coord_capture.find_iter(line).collect(); 
        let start: Vec<usize> = matches[0].as_str().split(",").map(|x: &str| x.parse::<usize>().unwrap()).collect();
        let end: Vec<usize> = matches[1].as_str().split(",").map(|x: &str| x.parse::<usize>().unwrap()).collect();
        let word: &str = word_matcher.find_iter(line).collect::<Vec<regex::Match<'_>>>()[0].as_str();

        for i in start[0]..end[0]+1 {
            for j in start[1]..end[1]+1 {
                match word {
                    "toggle" => grid[i][j] = (grid[i][j] + 1) % 2,
                    "off" => grid[i][j] = 0,
                    "on" => grid[i][j] = 1,
                    _ => ()
                }
            }
        }
    }

    let num_lit: i32 = grid.iter().map(|x: &[i32; 1000]| x.iter().sum()).collect::<Vec<i32>>().iter().sum();
    return num_lit;
}

fn part2(input: &String) -> i32 {
    let mut grid: [[i32; 1000]; 1000] = [[0; 1000]; 1000];
    let coord_capture: regex::Regex = regex::Regex::new(r"[0-9]*,[0-9]*").unwrap();
    let word_matcher: regex::Regex = regex::Regex::new(r"toggle|off|on").unwrap();

    for line in input.lines() {
        let matches: Vec<regex::Match<'_>> = coord_capture.find_iter(line).collect(); 
        let start: Vec<usize> = matches[0].as_str().split(",").map(|x: &str| x.parse::<usize>().unwrap()).collect();
        let end: Vec<usize> = matches[1].as_str().split(",").map(|x: &str| x.parse::<usize>().unwrap()).collect();
        let word: &str = word_matcher.find_iter(line).collect::<Vec<regex::Match<'_>>>()[0].as_str();

        for i in start[0]..end[0]+1 {
            for j in start[1]..end[1]+1 {
                match word {
                    "toggle" => grid[i][j] += 2,
                    "off" => if grid[i][j] > 0 { grid[i][j] -= 1 },
                    "on" => grid[i][j] += 1,
                    _ => ()
                }
            }
        }
    }

    let num_lit: i32 = grid.iter().map(|x: &[i32; 1000]| x.iter().sum()).collect::<Vec<i32>>().iter().sum();
    return num_lit;
}

pub fn solve(filepath: &String) {
    let input: String = fs::read_to_string(filepath).unwrap();

    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}