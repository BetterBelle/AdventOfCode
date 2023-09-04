use std::{ fs, fmt }; 
use std::collections::HashMap;
use regex;

enum Operation {
    LSHIFT,
    RSHIFT,
    AND,
    OR,
    NOT,
    IN
}
impl fmt::Display for Operation {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            Operation::LSHIFT => write!(f, "LSHIFT"),
            Operation::RSHIFT => write!(f, "RSHIFT"),
            Operation::AND => write!(f, "AND"),
            Operation::OR => write!(f, "OR"),
            Operation::NOT => write!(f, "NOT"),
            Operation::IN => write!(f, ""),
        }
    }
}

struct Instruction<'a> {
    lhs: Option<&'a str>,
    operation: &'a Operation,
    rhs: Option<&'a str>,
    target: &'a str 
}

impl<'a> Instruction<'a> {
    fn new(found_wires: Vec<&'a str>, values: Vec<&'a str>, operation: &'a Operation) -> Instruction<'a> {
        let lhs: Option<&str>;
        let rhs:Option<&str>; 
        let target: &str;

        match operation {
            Operation::LSHIFT | Operation::RSHIFT => {
                lhs = Some(found_wires[0]);
                rhs = Some(values[0]);
                target = found_wires[1];
            },
            Operation::AND | Operation::OR => {
                if found_wires.len() == 1 {
                    lhs = Some(values[0]);
                    rhs = Some(values[1]);
                    target = found_wires[0];
                } 
                else if found_wires.len() == 2 {
                    lhs = Some(found_wires[0]);
                    rhs = Some(values[0]);
                    target = found_wires[1];
                }
                else {
                    lhs = Some(found_wires[0]);
                    rhs = Some(found_wires[1]);
                    target = found_wires[2];
                }
            },
            Operation::NOT | Operation::IN => {
                if found_wires.len() == 1 {
                    lhs = None;
                    rhs = Some(values[0]);
                    target = found_wires[0]; 
                }
                else {
                    lhs = None;
                    rhs = Some(found_wires[0]);
                    target = found_wires[1];
                }
            }, 
        }
        return Instruction {
            lhs,
            operation,
            rhs,
            target
        }
    }
}

fn create_instruction_mapping() -> std::collections::HashMap<&'static str, Operation> {
    let mut instruction_mapping: std::collections::HashMap<&str, Operation> = std::collections::HashMap::new();
    instruction_mapping.insert("LSHIFT", Operation::LSHIFT);
    instruction_mapping.insert("RSHIFT", Operation::RSHIFT);
    instruction_mapping.insert("AND", Operation::AND);
    instruction_mapping.insert("OR", Operation::OR);
    instruction_mapping.insert("NOT", Operation::NOT);
    instruction_mapping.insert("IN", Operation::IN);
    return instruction_mapping;
}

fn perform_instructions(mut instructions: Vec<Instruction>) -> HashMap<&str, u16> {
    let mut wires: HashMap<&str, u16> = HashMap::new();
    // performs instructions in order
    let mut i: usize = 0;
    while instructions.len() > 0 {
        let inst: &Instruction<'_> = &instructions[i];
        let mut left_value: Option<u16> = None;
        let mut right_value: Option<u16> = None;
        let mut value_to_insert: Option<u16> = None;

        if let Some(_) = inst.lhs {
            match inst.lhs.unwrap().parse::<u16>() {
                Ok(v) => left_value = Some(v),
                Err(_) => { 
                    left_value = match wires.get(inst.lhs.unwrap()) {
                        Some(v) => Some(*v),
                        None => None 
                    }
                } 
            }
        }

        if let Some(_) = inst.rhs {
            match inst.rhs.unwrap().parse::<u16>() {
                Ok(v) => right_value = Some(v),
                Err(_) => { 
                    right_value = match wires.get(inst.rhs.unwrap()) {
                        Some(v) => Some(*v),
                        None => None 
                    }
                } 
            }
        }
        
        // do operation if possible
        match inst.operation {
            Operation::LSHIFT => if left_value != None && right_value != None { value_to_insert = Some(left_value.unwrap() << right_value.unwrap()) },
            Operation::RSHIFT => if left_value != None && right_value != None { value_to_insert = Some(left_value.unwrap() >> right_value.unwrap()) },
            Operation::AND => if left_value != None && right_value != None { value_to_insert = Some(left_value.unwrap() & right_value.unwrap()) },
            Operation::OR => if left_value != None && right_value != None { value_to_insert = Some(left_value.unwrap() | right_value.unwrap()) },
            Operation::NOT => if right_value != None { value_to_insert = Some(!right_value.unwrap()) },
            Operation::IN => if right_value != None { value_to_insert = Some(right_value.unwrap()) },
        }
        // if value to insert is valid, insert value to wires and remove the instruction
        match value_to_insert {
            Some(v) => {
                wires.insert(inst.target, v);
                instructions.remove(i);
                i = 0;
            },
            None => i += 1,
        }
    }
    return wires;
}

fn construct_instructions<'a>(input: &'a String, instruction_mapping: &'a HashMap<&'a str, Operation>) -> Vec<Instruction<'a>> {
    let wire_capture: regex::Regex = regex::Regex::new(r"[a-z]?[ $a-z]( |$)").unwrap();
    let operation_capture: regex::Regex = regex::Regex::new(r"LSHIFT|RSHIFT|AND|OR|NOT").unwrap();
    let value_capture: regex::Regex = regex::Regex::new(r"([0-9])+").unwrap();

    let mut instructions: Vec<Instruction> = Vec::new();

    // Construct instructions
    for line in input.lines() {

        let operator_match: Vec<regex::Match<'_>> = operation_capture.find_iter(line).collect();
        let operator_str: &str = if operator_match.len() > 0 { operator_match[0].as_str() } else { "IN" };
        let operation: &Operation = instruction_mapping.get(operator_str).unwrap();

        let value_matches: Vec<regex::Match<'_>> = value_capture.find_iter(line).collect();
        let values: Vec<&str> = value_matches.iter().map(|x: &regex::Match<'_>| x.as_str()).collect();

        let wire_matches: Vec<regex::Match<'_>> = wire_capture.find_iter(line).collect();
        let found_wires: Vec<&str> = wire_matches.iter().map(|x: &regex::Match<'_>| x.as_str().trim()).collect();
        instructions.push(Instruction::new(found_wires, values, operation));

    }

    return instructions;
}

fn part1(input: &String) -> u16 {
    let instruction_mapping: HashMap<&str, Operation> = create_instruction_mapping();
    let instructions = construct_instructions(input, &instruction_mapping);
    let wires: HashMap<&str, u16> = perform_instructions(instructions); 
    return *wires.get("a").unwrap();
}

fn part2(input: &String, previous_answer: &str) -> u16 {
    let instruction_mapping: HashMap<&str, Operation> = create_instruction_mapping();
    let mut instructions: Vec<Instruction<'_>> = construct_instructions(input, &instruction_mapping);
    for inst in instructions.iter_mut() {
        if inst.target == "b" {
            inst.rhs = Some(previous_answer);
        }
    }
    let wires: HashMap<&str, u16> = perform_instructions(instructions); 
    return *wires.get("a").unwrap();
}

pub fn solve(filepath: &String) {
    let input: String = fs::read_to_string(filepath).unwrap();
    let part1: u16 = part1(&input);
    println!("Part 1: {}", part1);
    println!("Part 2: {}", part2(&input, part1.to_string().as_str()));
}