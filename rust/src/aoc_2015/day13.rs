use std::collections::HashMap;
use std::fs;

fn construct_graph(input: &String, part: i32) -> HashMap<&str, HashMap<&str, i32>> {
    let mut people: HashMap<&str, HashMap<&str, i32>> = HashMap::new();
    if part == 2 {
        people.insert("Annabelle", HashMap::new());
    }

    let important_char_finder: regex::Regex =
        regex::Regex::new(r"Alice|Bob|Carol|David|Eric|Frank|George|Mallory|[0-9]+|lose|gain")
            .unwrap();

    // construct graph
    for line in input.lines() {
        let matches: Vec<regex::Match<'_>> = important_char_finder.find_iter(line).collect();
        let mut matched_as_string: Vec<&str> = matches
            .iter()
            .map(|x: &regex::Match<'_>| x.as_str())
            .collect();

        let person: &str = matched_as_string.pop().unwrap();
        let happiness_amount: i32 = matched_as_string.pop().unwrap().parse::<i32>().unwrap();
        let happiness: i32 = if matched_as_string.pop().unwrap() == "lose" {
            happiness_amount * -1
        } else {
            happiness_amount
        };
        let original_person: &str = matched_as_string.pop().unwrap();

        match people.get_mut(original_person) {
            Some(v) => {
                let _ = v.insert(person, happiness);
            }
            None => {
                people.insert(original_person, HashMap::new());
                people
                    .get_mut(original_person)
                    .unwrap()
                    .insert(person, happiness);
                if part == 2 {
                    people
                        .get_mut(original_person)
                        .unwrap()
                        .insert("Annabelle", 0);
                    people
                        .get_mut("Annabelle")
                        .unwrap()
                        .insert(original_person, 0);
                }
            }
        }
    }

    return people;
}

fn trace_path_value(path: &mut Vec<&str>, graph: &HashMap<&str, HashMap<&str, i32>>) -> i32 {
    let mut path_value = 0;
    for i in 0..path.len() {
        let val1 = graph
            .get(path[i])
            .unwrap()
            .get(path[(i + 1) % path.len()])
            .unwrap();
        path_value += val1;

        let val2 = graph
            .get(path[(i + 1) % path.len()])
            .unwrap()
            .get(path[i])
            .unwrap();
        path_value += val2;
    }

    return path_value;
}

fn get_path_lengths(graph: &HashMap<&str, HashMap<&str, i32>>) -> i32 {
    let mut visited: HashMap<&str, bool> = HashMap::new();
    for person in graph.keys() {
        visited.insert(person, false);
    }
    let mut path: Vec<&str> = Vec::new();
    let mut path_lengths: Vec<i32> = Vec::new();
    trace_paths(
        &String::from("Alice"),
        &mut visited,
        &mut path,
        &graph,
        &mut path_lengths,
    );

    return *path_lengths.iter().max().unwrap();
}

fn trace_paths<'a>(
    start: &'a str,
    visited: &mut HashMap<&'a str, bool>,
    path: &mut Vec<&'a str>,
    graph: &'a HashMap<&str, HashMap<&str, i32>>,
    path_lengths: &mut Vec<i32>,
) {
    visited.insert(start, true);
    path.push(start);

    if path.len() == graph.keys().len() {
        path_lengths.push(trace_path_value(path, graph));
    } else {
        for next_node in graph.get(start).unwrap().keys() {
            if !visited.get(next_node).unwrap() {
                trace_paths(&next_node, visited, path, graph, path_lengths);
            }
        }
    }

    path.pop();
    visited.insert(start, false);
}

fn part1(input: &String) -> i32 {
    let people = construct_graph(input, 1);
    return get_path_lengths(&people);
}

fn part2(input: &String) -> i32 {
    let people = construct_graph(input, 2);
    return get_path_lengths(&people);
}

pub fn solve(filepath: &String) {
    let input: String = fs::read_to_string(filepath).unwrap();

    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}
