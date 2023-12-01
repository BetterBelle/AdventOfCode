use std::fs;
use regex;

fn is_valid(password: &String) -> bool {
    // finds the consecutive letters in the strings
    let consecutive_char_finder: regex::Regex = regex::Regex::new(r"abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz").unwrap();
    // i o and l are illegal characters
    let illegal_char_finder: regex::Regex = regex::Regex::new(r"i|o|l").unwrap();
    // finds pairs of characters but ignores triplets
    let find_distinct_repeated_pair: fancy_regex::Regex = fancy_regex::Regex::new(r"(.)\1").unwrap();

    let num_consecutive_matches: u32 = consecutive_char_finder.find_iter(password).count() as u32;
    let num_illegal_chars: u32 = illegal_char_finder.find_iter(password).count() as u32;
    let num_distinct_pairs: u32 = find_distinct_repeated_pair.find_iter(password).count() as u32;

    if num_consecutive_matches >= 1 && num_illegal_chars == 0 && num_distinct_pairs >= 2 {
        return true;
    }

    return false;
}


fn increment(s: &String) -> String {
    let mut str_vec: Vec<u8> = s.chars().map(|x: char| x as u8).collect();
    let mut i = str_vec.len() - 1;
    let mut overflow = true;

    while overflow {
        // overflow is false by default every time
        overflow = false;
        str_vec[i] += 1;
        // small z is 122, so if we overflow this will set it to 0
        str_vec[i] %= 123;
        if str_vec[i] == 0 {
            // 97 is an 'a'
            str_vec[i] += 97;
            overflow = true;
            // send i back one index to increment the next character
            i -= 1;
        }
    }

    let new_string: String = String::from_utf8(str_vec).unwrap();

    return new_string;
}

fn part1(input: &String) -> String {
    let mut password: String = input.clone().trim().to_string();
    // this is brute force and really slow
    // you can actually just do this in your head
    while !is_valid(&password) {
        password = increment(&password);
    }

    return password;
}

fn part2(input: &String) -> String {
    let mut password: String = input.clone().trim().to_string();
    // this is brute force and really slow
    // you can actually just do this in your head
    while !is_valid(&password) {
        password = increment(&password);
    }

    return password;
}

pub fn solve(filepath: &String) {
    let input: String = fs::read_to_string(filepath).unwrap();
    let part1_solution: String = part1(&input);

    println!("Part 1: {}", part1_solution);
    let part1_solution_inc: String = increment(&String::from(&part1_solution));
    
    // my part1 solution, incremented by 1 for part 2
    // let part1_solution_inc: String = increment(&String::from("vzbxxyzz"));

    println!("Part 2: {}", part2(&part1_solution_inc));
}
