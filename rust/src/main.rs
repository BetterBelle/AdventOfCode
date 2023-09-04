// ngl, rust annoys me that it won't allow just numbers for the modules, but that's life I guess
use std::env;
mod aoc_2015;
fn main() {
    let args: Vec<String> = env::args().collect();

    let mut year: i32 = 2015;
    let mut day: i32 = 1;

    for (i, word) in args.iter().enumerate() {
        match word.as_str() {
            "-y" => year = args[i+1].parse::<i32>().unwrap(),
            "-d" => day = args[i+1].parse::<i32>().unwrap(),
            _ => ()
        }
    }

    // filepath constructed and will be passed into functions for parsing or further reconstruction
    let filepath: String = format!("../{}/day{:02}.txt", year, day);

    match (year, day) {
        (2015, 1) =>  aoc_2015::day01::solve(&filepath),
        (2015, 2) =>  aoc_2015::day02::solve(&filepath),
        (2015, 3) =>  aoc_2015::day03::solve(&filepath),
        (2015, 4) =>  aoc_2015::day04::solve(&filepath),
        (2015, 5) =>  aoc_2015::day05::solve(&filepath),
        (2015, 6) =>  aoc_2015::day06::solve(&filepath),
        (2015, 7) =>  aoc_2015::day07::solve(&filepath),
        // (2015, 8) =>  aoc_2015::day08::solve(&filepath),
        // (2015, 9) =>  aoc_2015::day09::solve(&filepath),
        // (2015, 10) => aoc_2015::day10::solve(&filepath),
        // (2015, 11) => aoc_2015::day11::solve(&filepath),
        // (2015, 12) => aoc_2015::day12::solve(&filepath),
        // (2015, 13) => aoc_2015::day13::solve(&filepath),
        // (2015, 14) => aoc_2015::day14::solve(&filepath),
        // (2015, 15) => aoc_2015::day15::solve(&filepath),
        // (2015, 16) => aoc_2015::day16::solve(&filepath),
        // (2015, 17) => aoc_2015::day17::solve(&filepath),
        // (2015, 18) => aoc_2015::day18::solve(&filepath),
        // (2015, 19) => aoc_2015::day19::solve(&filepath),
        // (2015, 20) => aoc_2015::day20::solve(&filepath),
        // (2015, 21) => aoc_2015::day21::solve(&filepath),
        // (2015, 22) => aoc_2015::day22::solve(&filepath),
        // (2015, 23) => aoc_2015::day23::solve(&filepath),
        // (2015, 24) => aoc_2015::day24::solve(&filepath),
        // (2015, 25) => aoc_2015::day25::solve(&filepath),
        // (2016, 1) =>  aoc_2016::day01::solve(&filepath),
        // (2016, 2) =>  aoc_2016::day02::solve(&filepath),
        // (2016, 3) =>  aoc_2016::day03::solve(&filepath),
        // (2016, 4) =>  aoc_2016::day04::solve(&filepath),
        // (2016, 5) =>  aoc_2016::day05::solve(&filepath),
        // (2016, 6) =>  aoc_2016::day06::solve(&filepath),
        // (2016, 7) =>  aoc_2016::day07::solve(&filepath),
        // (2016, 8) =>  aoc_2016::day08::solve(&filepath),
        // (2016, 9) =>  aoc_2016::day09::solve(&filepath),
        // (2016, 10) => aoc_2016::day10::solve(&filepath),
        // (2016, 11) => aoc_2016::day11::solve(&filepath),
        // (2016, 12) => aoc_2016::day12::solve(&filepath),
        // (2016, 13) => aoc_2016::day13::solve(&filepath),
        // (2016, 14) => aoc_2016::day14::solve(&filepath),
        // (2016, 15) => aoc_2016::day15::solve(&filepath),
        // (2016, 16) => aoc_2016::day16::solve(&filepath),
        // (2016, 17) => aoc_2016::day17::solve(&filepath),
        // (2016, 18) => aoc_2016::day18::solve(&filepath),
        // (2016, 19) => aoc_2016::day19::solve(&filepath),
        // (2016, 20) => aoc_2016::day20::solve(&filepath),
        // (2016, 21) => aoc_2016::day21::solve(&filepath),
        // (2016, 22) => aoc_2016::day22::solve(&filepath),
        // (2016, 23) => aoc_2016::day23::solve(&filepath),
        // (2016, 24) => aoc_2016::day24::solve(&filepath),
        // (2016, 25) => aoc_2016::day25::solve(&filepath),
        _ => ()
    }
}
