use std::fs; 

fn perform_sequence(input: &String, amount: u32) -> u32 {
    let mut current_string: Vec<u32> = input.chars().map(|x: char| x.to_digit(10).unwrap()).collect();

    for _ in 0..amount {
        let mut current_digit: u32 = current_string[0];
        let mut next_string: Vec<u32> = Vec::new();
        let mut j: usize = 1;
        let mut current_len: u32 = 1;

        while j < current_string.len() {
            // checking if the string is being increased
            // when the sequence is broken, insert into next string and reset vars
            if current_digit != current_string[j] {
                next_string.push(current_len);
                next_string.push(current_digit);
                current_digit = current_string[j];
                current_len = 1;
            }
            // otherwise increase the length of the current sequence for insertion to next string
            else {
                current_len += 1;
            }
            j += 1;
        }
        // once done, insert the last thing done into the next string because we terminate
        // right as we go out of bounds, so if we end on a sequence (we always do), that sequence doesn't get inserted
        next_string.push(current_len);
        next_string.push(current_digit);

        // once we've made it through the whole previous string, set current string to next string
        current_string = next_string;
    }

    return current_string.len() as u32;
}

fn part1(input: &String) -> u32 {
    return perform_sequence(input, 40);
}

fn part2(input: &String) -> u32 {
    return perform_sequence(input, 50);
}

pub fn solve(filepath: &String) {
    let input: String = fs::read_to_string(filepath).unwrap();
    
    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}
