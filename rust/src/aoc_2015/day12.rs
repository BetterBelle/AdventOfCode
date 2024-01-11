use regex;
use std::fs;

struct Record {
    obj: String,
    sum: i32,
    red: bool,
}

fn part1(input: &String) -> i32 {
    let number_finder: regex::Regex = regex::Regex::new(r"-?[0-9]+").unwrap();
    let number_matches: Vec<regex::Match<'_>> = number_finder.find_iter(input).collect();
    let numbers: Vec<i32> = number_matches
        .iter()
        .map(|x: &regex::Match<'_>| x.as_str().parse::<i32>().unwrap())
        .collect();

    let mut sum = 0;

    for num in numbers {
        sum += num;
    }

    return sum;
}

fn part2(input: &String) -> i32 {
    let important_char_finder: regex::Regex =
        regex::Regex::new(r"-?[0-9]+|(\{|})|red|\[|]").unwrap();
    let matches: Vec<regex::Match<'_>> = important_char_finder.find_iter(input).collect();
    let matched_as_string: Vec<&str> = matches
        .iter()
        .map(|x: &regex::Match<'_>| x.as_str())
        .collect();

    // keeps track of the current depth of nesting
    let mut depth_track: Vec<Record> = vec![];
    let mut sum = 0;

    for matched in matched_as_string {
        match matched {
            // red is ignored if in an object, but not an array
            "red" => {
                let mut last_record = depth_track.pop().unwrap();
                if last_record.obj == "obj" {
                    last_record.red = true;
                }
                depth_track.push(last_record);
            }
            "{" => {
                depth_track.push(Record {
                    obj: String::from("obj"),
                    sum: 0,
                    red: false,
                });
            }
            "}" => {
                // if it's a non-red record depth that's being closed, we
                // add it's sum to the previous depth and
                let last_record = depth_track.pop().unwrap();
                if !last_record.red {
                    match depth_track.pop() {
                        Some(mut record) => {
                            record.sum += last_record.sum;
                            depth_track.push(record);
                        }
                        None => {
                            sum += last_record.sum;
                        }
                    };
                }
            }
            "[" => depth_track.push(Record {
                obj: String::from("arr"),
                sum: 0,
                red: false,
            }),
            "]" => {
                // pop the record, then add to the previous one
                // if this is the last record on the stack, instead just add to the sum
                let last_record = depth_track.pop().unwrap();
                match depth_track.pop() {
                    Some(mut record) => {
                        record.sum += last_record.sum;
                        depth_track.push(record);
                    }
                    None => {
                        sum += last_record.sum;
                    }
                };
            }
            // this means we matched a number
            _ => {
                let num = matched.parse::<i32>().unwrap();
                let mut last_record = depth_track.pop().unwrap();
                last_record.sum += num;
                depth_track.push(last_record);
            }
        }
    }

    return sum;
}

pub fn solve(filepath: &String) {
    let input: String = fs::read_to_string(filepath).unwrap();

    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}
