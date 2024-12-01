use std::fs;

#[derive(Debug)]
struct Sue {
    id: Option<i32>,
    children: Option<i32>,
    cats: Option<i32>,
    samoyeds: Option<i32>,
    pomeranians: Option<i32>,
    akitas: Option<i32>,
    vizslas: Option<i32>,
    goldfish: Option<i32>,
    trees: Option<i32>,
    cars: Option<i32>,
    perfumes: Option<i32>,
}

impl Sue {
    pub fn new(
        id: Option<i32>,
        children: Option<i32>,
        cats: Option<i32>,
        samoyeds: Option<i32>,
        pomeranians: Option<i32>,
        akitas: Option<i32>,
        vizslas: Option<i32>,
        goldfish: Option<i32>,
        trees: Option<i32>,
        cars: Option<i32>,
        perfumes: Option<i32>,
    ) -> Sue {
        return Sue {
            id,
            children,
            cats,
            samoyeds,
            pomeranians,
            akitas,
            vizslas,
            goldfish,
            trees,
            cars,
            perfumes,
        };
    }
}

fn create_sue(line: String) -> Sue {
    let number_matcher: regex::Regex = regex::Regex::new(r"[0-9]+").unwrap();
    let word_matcher: regex::Regex = regex::Regex::new(r"Sue|children|cats|samoyeds|pomeranians|akitas|vizslas|goldfish|trees|cars|perfumes").unwrap();

    let number_matches: Vec<regex::Match<'_>> = number_matcher.find_iter(&line).collect();
    let word_matches: Vec<regex::Match<'_>> = word_matcher.find_iter(&line).collect();

    let numbers: Vec<i32> = number_matches.iter().map(|x: &regex::Match<'_>| x.as_str().parse::<i32>().unwrap()).collect();
    let words: Vec<String> = word_matches.iter().map(|x: &regex::Match<'_>| String::from(x.as_str())).collect();
    
    let mut id : Option<i32> = None;
    let mut children : Option<i32> = None;
    let mut cats : Option<i32> = None;
    let mut samoyeds : Option<i32> = None;
    let mut pomeranians : Option<i32> = None;
    let mut akitas : Option<i32> = None;
    let mut vizslas : Option<i32> = None;
    let mut goldfish : Option<i32> = None;
    let mut trees : Option<i32> = None;
    let mut cars : Option<i32> = None;
    let mut perfumes : Option<i32> = None;

    for i in 0..words.len() {
        match words[i].as_str() {
            "Sue" => { id = Some(numbers[i]) },
            "children" => { children = Some(numbers[i]) },
            "cats" => { cats = Some(numbers[i]) },
            "samoyeds" => { samoyeds = Some(numbers[i]) },
            "pomeranians" => { pomeranians = Some(numbers[i]) },
            "akitas" => { akitas = Some(numbers[i]) },
            "vizslas" => { vizslas = Some(numbers[i]) },
            "goldfish" => { goldfish = Some(numbers[i]) },
            "trees" => { trees = Some(numbers[i]) },
            "cars" => { cars = Some(numbers[i]) },
            "perfumes" => { perfumes = Some(numbers[i]) },
            _ => { 
                println!("Something went wrong!"); 
                std::process::exit(1);
            },
        }
    }
    return Sue::new(id, children, cats, samoyeds, pomeranians, akitas, vizslas, goldfish, trees, cars, perfumes);
}

fn part1(real_sue: &Sue, sues: &Vec<Sue>) -> i32 {
    let mut matching_sues: Vec<&Sue> = Vec::new();
    for sue in sues {
        let mut matched_sue = true;
        match sue.children {
            Some(n) => if real_sue.children.unwrap() != n { matched_sue = false; },
            None => (),
        }
        match sue.cats {
            Some(n) => if real_sue.cats.unwrap() != n { matched_sue = false; },
            None => (),
        }
        match sue.samoyeds {
            Some(n) => if real_sue.samoyeds.unwrap() != n { matched_sue = false; },
            None => (),
        }
        match sue.pomeranians {
            Some(n) => if real_sue.pomeranians.unwrap() != n { matched_sue = false; },
            None => (),
        }
        match sue.akitas {
            Some(n) => if real_sue.akitas.unwrap() != n { matched_sue = false; },
            None => (),
        }
        match sue.vizslas {
            Some(n) => if real_sue.vizslas.unwrap() != n { matched_sue = false; },
            None => (),
        }
        match sue.goldfish {
            Some(n) => if real_sue.goldfish.unwrap() != n { matched_sue = false; },
            None => (),
        }
        match sue.trees {
            Some(n) => if real_sue.trees.unwrap() != n { matched_sue = false; },
            None => (),
        }
        match sue.cars {
            Some(n) => if real_sue.cars.unwrap() != n { matched_sue = false; },
            None => (),
        }
        match sue.perfumes {
            Some(n) => if real_sue.perfumes.unwrap() != n { matched_sue = false; },
            None => (),
        }

        if matched_sue { matching_sues.push(sue) }
    }
    if matching_sues.len() != 1 {
        println!("Something went wrong!");
        std::process::exit(1);
    }

    let correct_sue: &Sue = matching_sues.pop().unwrap();
    return correct_sue.id.unwrap();
}

fn part2(real_sue: &Sue, sues: &Vec<Sue>) -> i32 {
    let mut matching_sues: Vec<&Sue> = Vec::new();
    for sue in sues {
        let mut matched_sue = true;
        match sue.children {
            Some(n) => if real_sue.children.unwrap() != n { matched_sue = false; },
            None => (),
        }
        match sue.cats {
            Some(n) => if real_sue.cats.unwrap() >= n { matched_sue = false; },
            None => (),
        }
        match sue.samoyeds {
            Some(n) => if real_sue.samoyeds.unwrap() != n { matched_sue = false; },
            None => (),
        }
        match sue.pomeranians {
            Some(n) => if real_sue.pomeranians.unwrap() <= n { matched_sue = false; },
            None => (),
        }
        match sue.akitas {
            Some(n) => if real_sue.akitas.unwrap() != n { matched_sue = false; },
            None => (),
        }
        match sue.vizslas {
            Some(n) => if real_sue.vizslas.unwrap() != n { matched_sue = false; },
            None => (),
        }
        match sue.goldfish {
            Some(n) => if real_sue.goldfish.unwrap() <= n { matched_sue = false; },
            None => (),
        }
        match sue.trees {
            Some(n) => if real_sue.trees.unwrap() >= n { matched_sue = false; },
            None => (),
        }
        match sue.cars {
            Some(n) => if real_sue.cars.unwrap() != n { matched_sue = false; },
            None => (),
        }
        match sue.perfumes {
            Some(n) => if real_sue.perfumes.unwrap() != n { matched_sue = false; },
            None => (),
        }

        if matched_sue { matching_sues.push(sue) }
    }
    if matching_sues.len() != 1 {
        println!("{:?}", matching_sues);
        println!("Something went wrong!");
        std::process::exit(1);
    }

    let correct_sue: &Sue = matching_sues.pop().unwrap();
    return correct_sue.id.unwrap();
}

pub fn solve(filepath: &String) {
    let input: String = fs::read_to_string(filepath).unwrap();
    let real_sue: Sue = Sue::new(None, Some(3), Some(7), Some(2), Some(3), Some(0), Some(0), Some(5), Some(3), Some(2), Some(1));
    let mut sues: Vec<Sue> = Vec::new();

    for line in input.lines() {
        sues.push(create_sue(String::from(line)));
    }

    println!("Part 1: {}", part1(&real_sue, &sues));
    println!("Part 2: {}", part2(&real_sue, &sues));
}
