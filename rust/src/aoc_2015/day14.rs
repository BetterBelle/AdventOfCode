use std::fs;
use std::cmp;

#[derive(Debug)]
enum State {
    Fly,
    Rest
}

#[derive(Debug)]
struct Reindeer {
    speed: i32,
    fly: i32,
    rest: i32,
    distance: i32,
    time_flying: i32,
    time_resting: i32,
    state: State,
    score: i32
}

impl Reindeer {
    pub fn new(speed_in: &str, fly_in: &str, rest_in: &str) -> Reindeer {
        let speed = speed_in.parse::<i32>().unwrap();
        let fly = fly_in.parse::<i32>().unwrap();
        let rest = rest_in.parse::<i32>().unwrap();

        return Reindeer { 
            speed, 
            fly, 
            rest, 
            distance : 0, 
            time_flying : 0, 
            time_resting : 0, 
            state : State::Fly,
            score : 0
        };
    }

    pub fn reset(&mut self) {
        self.distance = 0;
        self.time_flying = 0;
        self.time_resting = 0;
        self.state = State::Fly;
        self.score = 0;
    }

    pub fn race(&mut self, time: i32) {
        let mut timer = 0;
        while timer < time {
            match self.state {
                State::Fly => {
                    self.state = State::Rest;
                    self.time_flying += cmp::min(time - timer, self.fly);
                    timer += cmp::min(time - timer, self.fly);
                },
                State::Rest => {
                    self.state = State::Fly;
                    timer += cmp::min(time - timer, self.rest);
                }
            }
        }
        self.distance = self.time_flying * self.speed;
    }

    pub fn step(&mut self) {
        match self.state {
            State::Fly => {
                self.distance += self.speed;
                self.time_flying = (self.time_flying + 1) % self.fly;
                if self.time_flying == 0 {
                    self.state = State::Rest;
                }
            },
            State::Rest => {
                self.time_resting = (self.time_resting + 1) % self.rest;
                if self.time_resting == 0 {
                    self.state = State::Fly;
                }
            },
        }        
    }

    pub fn score(&mut self, max: i32) {
        if self.distance == max {
            self.score += 1;
        }
    }
}

fn create_reindeer(input: String) -> Vec<Reindeer> {
    let number_matcher: regex::Regex = regex::Regex::new(r"[A-Z][a-z]+|[0-9]+").unwrap();
    let matches: Vec<regex::Match<'_>> = number_matcher
        .find_iter(&input).collect();
    let matched_as_string: Vec<&str> = matches
        .iter()
        .map(|x: &regex::Match<'_>| x.as_str())
        .collect();

    let mut reindeer: Vec<Reindeer> = Vec::new();

    for i in (0..matched_as_string.len()/4).into_iter().map(|x| x * 4) {
        reindeer.push(
            Reindeer::new(
                matched_as_string[i+1],
                matched_as_string[i+2],
                matched_as_string[i+3]
            )
        );
    }
    return reindeer;
}

union Func {
   f1: fn(&mut Reindeer),
   f2: fn(&mut Reindeer, i32)
}

fn apply_on_reindeer(reindeer: &mut Vec<Reindeer>, func: Func, value: Option<i32>) { 
    unsafe {
        match value {
            Some(v) => {
                for r in reindeer.iter_mut() {
                    (func.f2)(r, v);
                }
            },
            None => {
                for r in reindeer.iter_mut() {
                    (func.f1)(r);
                }
            },
        }
    }
}

fn part1(reindeer: &mut Vec<Reindeer>) -> i32 {
    apply_on_reindeer(reindeer, Func { f2: Reindeer::race }, Some(2503));
    let winner = reindeer.iter().reduce(|x: &Reindeer, y: &Reindeer| if x.distance > y.distance { x } else { y }).unwrap();
    return winner.distance;
}

fn part2(reindeer: &mut Vec<Reindeer>) -> i32 {
    for _ in 0..2503 {
        apply_on_reindeer(reindeer, Func { f1: Reindeer::step }, None);
        let max: i32 = reindeer.iter().reduce(|x: &Reindeer, y: &Reindeer| if x.distance > y.distance { x } else { y }).unwrap().distance;
        apply_on_reindeer(reindeer, Func { f2: Reindeer::score }, Some(max));
    }

    let winner = reindeer.iter().reduce(|x: &Reindeer, y: &Reindeer| if x.score > y.score { x } else { y }).unwrap();
    return winner.score;
}

pub fn solve(filepath: &String) {
    let input: String = fs::read_to_string(filepath).unwrap();
    let mut reindeer: Vec<Reindeer> = create_reindeer(input);

    apply_on_reindeer(&mut reindeer, Func { f1: Reindeer::reset }, None);
    println!("Part 1: {}", part1(&mut reindeer));
    apply_on_reindeer(&mut reindeer, Func { f1: Reindeer::reset }, None);
    println!("Part 2: {}", part2(&mut reindeer));
}
