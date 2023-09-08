use std::fs; 
use regex;

fn part1(input: &String) -> u32 {
    let mut total_chars: u32 = 0;
    let mut num_chars: u32 = 0;
    let escaped_char_finder: regex::Regex = regex::Regex::new(r#"\\x[a-f0-9]{2}|\\["'\\]"#).unwrap();

    for line in input.lines() {
        total_chars += line.len() as u32;

        let found_escaped: Vec<regex::Match<'_>> = escaped_char_finder.find_iter(line).collect();
        let escaped_chars: Vec<&str> = found_escaped.iter().map(|x: &regex::Match<'_>| x.as_str()).collect();
        // escaped characters are all strings, get their length - 1 to determine how much space they take for 1 character
        let escaped_chars_len: Vec<u32> = escaped_chars.iter().map(|x: &&str| x.len() as u32 - 1).collect();
        let num_escaped_chars: u32 = escaped_chars_len.iter().sum();

        // the extra - 2 is for the encapsulating " characters
        let actual_string_length: u32 = line.len() as u32 - num_escaped_chars - 2;
        num_chars += actual_string_length;
    }

    return total_chars - num_chars;
}

fn part2(input: &String) -> u32 {
    let mut total_chars: u32 = 0;
    let mut new_total_chars: u32 = 0;
    let chars_to_escape_finder: regex::Regex = regex::Regex::new(r#"[\\"']"#).unwrap();

    for line in input.lines() {
        total_chars += line.len() as u32;

        let found_to_escape: Vec<regex::Match<'_>> = chars_to_escape_finder.find_iter(line).collect();
        let to_escape_chars: Vec<&str> = found_to_escape.iter().map(|x: &regex::Match<'_> | x.as_str()).collect();
        let num_escapes: u32 = to_escape_chars.len() as u32;

        
        println!("{} : {:?} : {}", line, to_escape_chars, num_escapes);
        // + 2 for extra quotes around new string
        new_total_chars += line.len() as u32 + num_escapes + 2;
    }

    return new_total_chars - total_chars;
}

pub fn solve(filepath: &String) {
    let input: String = fs::read_to_string(filepath).unwrap();
    
    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}