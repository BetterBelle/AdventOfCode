use std::fs; 
use std::collections::HashMap;
use itertools::Itertools;

#[derive(Debug)]
struct Destination<'a> {
    name: &'a str,
    distance: u32
}

fn construct_graph(input: &String) -> HashMap<&str, Vec<Destination<'_>>> {
    // keeping in mind this graph is undirected
    let mut graph: HashMap<&str, Vec<Destination>> = HashMap::new(); 

    // constructs the graph
    for line in input.lines() {
        let line_split: Vec<&str> = line.split(" ").collect();
        // 0 is source, 2 is destination, 4 is distance, insert each end to the other to ensure both directions valid
        let source: &str = line_split[0];
        let destination: &str = line_split[2];
        let distance: u32 = line_split[4].parse::<u32>().unwrap();

        let source_dest: Destination = Destination { name: source, distance: distance };
        let dest_dest: Destination = Destination { name: destination, distance: distance };

        // if source is a key, push the destination, otherwise insert the source and vector, then push
        if let Some(insertion) = graph.get_mut(source) {
            insertion.push(dest_dest); 
        } else {
            graph.insert(source, Vec::new());
            graph.get_mut(source).unwrap().push(dest_dest);
        }

        // same thing but with the "destination"
        if let Some(insertion) = graph.get_mut(destination) {
            insertion.push(source_dest);
        } else {
            graph.insert(destination, Vec::new());
            graph.get_mut(destination).unwrap().push(source_dest);
        }
    }

    return graph;
}

fn part1(input: &String) -> u32 {
    let graph: HashMap<&str, Vec<Destination<'_>>> = construct_graph(input);

    // create every possible path
    // do this using some basic combinatorics because the graph is complete
    let mut shortest_path: u32 = u32::MAX;
    for perm in graph.keys().permutations(graph.len()).unique() {
        // compute path length by traversing graph from a permutation
        let mut current_distance = 0;
        for (i, node) in perm.iter().enumerate() {
            if i < perm.len() - 1 {
                for dest in graph.get(*node).unwrap() {
                    if dest.name == *perm[i + 1] {
                        current_distance += dest.distance;
                    }
                }
            }
        }
        shortest_path = if current_distance < shortest_path { current_distance } else { shortest_path };
    }

    return shortest_path;
}

fn part2(input: &String) -> u32 {
    let graph: HashMap<&str, Vec<Destination<'_>>> = construct_graph(input);

    // create every possible path
    // do this using some basic combinatorics because the graph is complete
    let mut longest_path: u32 = u32::MIN;
    for perm in graph.keys().permutations(graph.len()).unique() {
        // compute path length by traversing graph from a permutation
        let mut current_distance = 0;
        for (i, node) in perm.iter().enumerate() {
            if i < perm.len() - 1 {
                for dest in graph.get(*node).unwrap() {
                    if dest.name == *perm[i + 1] {
                        current_distance += dest.distance;
                    }
                }
            }
        }
        longest_path = if current_distance > longest_path { current_distance } else { longest_path };
    }

    return longest_path;
}

pub fn solve(filepath: &String) {
    let input: String = fs::read_to_string(filepath).unwrap();
    
    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}