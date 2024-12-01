use std::{fs, process::exit};

fn input_to_grid(input: &String) -> Vec<Vec<i32>> {
    let mut grid: Vec<Vec<i32>> = Vec::new();
    let mut lines = input.lines();

    while let Some(line) = lines.next() {
        let mut new_line: Vec<i32> = Vec::new();
        for i in 0..line.len() {
            match line.as_bytes()[i] {
                b'.' => new_line.push(0),
                b'#' => new_line.push(1),
                _ => {
                    println!("Something is wrong with the input!");
                    exit(1);
                }
            }
        }

        grid.push(new_line);
    }

    return grid;
}

fn perform_conway(input_grid: &Vec<Vec<i32>>, output_grid: &mut Vec<Vec<i32>>, rear_offset: usize, pad_amount: usize, kernel: Vec<Vec<i32>>) {
    for i in 0..input_grid.len() - rear_offset {
        for j in 0..input_grid[i].len() - rear_offset {
            // grab slice
            let slice: Vec<Vec<&i32>> = input_grid 
                .iter()
                .skip(i)
                .take(kernel.len())
                .map(|s| s.iter().skip(j).take(kernel.len()).collect::<Vec<_>>())
                .collect::<Vec<_>>();

            // println!("{:?}", slice);

            // performs convolution
            let sum: i32 = slice
                .iter()
                .zip(&kernel) // zip slice and kernel
                .map(|(&ref s, k)| s.iter().zip(k).map(|(&x, y)| x * y).collect::<Vec<_>>()) // multiply
                // itemwise
                .collect::<Vec<_>>()
                .iter()
                .flat_map(|x| x.iter()) // flatten and sum
                .sum();

            // println!("SUM : {}", sum);
            // println!("CURRENT : {}", current_grid[i + pad_amount][j + pad_amount]);

            if sum == 3 || (sum == 2 && input_grid[i + pad_amount][j + pad_amount] == 1)  {
                output_grid[i][j] = 1;
            }
            else {
                output_grid[i][j] = 0;
            }

            // println!("{}", new_grid[i][j]);
        }
    }
}

fn turn_on_corners(vector: &mut Vec<Vec<i32>>) {
    let vector_len: usize = vector.len();
    let line_len: usize = vector[0].len();

    vector[0][0] = 1;
    vector[0][vector_len - 1] = 1;
    vector[vector_len - 1][0] = 1;
    vector[vector_len - 1][vector_len - 1] = 1;
}

fn pad_vector(vector: &mut Vec<Vec<i32>>, amount: i32) {
    // println!("--------- BEFORE ---------");
    // println!("LENGTH: {}", vector.len());
    // println!("LINE LENGTHS:");
    // for line in vector.iter() {
    //     print!("{}, ", line.len());
    // }
    // println!("\nACTUAL VECTOR:");
    // for line in vector.iter() {
    //     println!("{:?}", line);
    // }

    for line in vector.iter_mut() {
        for _ in 0..amount {
            line.insert(0, 0);
            line.push(0);
        }
    }
    for _ in 0..amount {
        vector.insert(0, vec![0; vector[1].len()]);
        vector.push(vec![0; vector[1].len()]);
    }

    // println!("--------- AFTER ---------");
    // println!("LENGTH: {}", vector.len());
    // println!("LINE LENGTHS:");
    // for line in vector.iter() {
    //     print!("{}, ", line.len());
    // }
    // println!("\nACTUAL VECTOR:");
    // for line in vector.iter() {
    //     println!("{:?}", line);
    // }
}

fn part1(starting_grid: &Vec<Vec<i32>>, steps: i32) -> i32 {
    let mut current_grid = starting_grid.clone();

    for _ in 0..steps {
        // to make convolution easier, add an extra 0 column to start and end, as well as extra
        // rows at top and bottom
        let mut new_grid = vec![vec![0; current_grid[0].len()]; current_grid.len()];
        let kernel: Vec<Vec<i32>> = vec![vec![1, 1, 1], vec![1, 0, 1], vec![1, 1, 1]];
        let rear_offset = kernel.len() - 1;
        let pad_amount = rear_offset / 2;
        pad_vector(&mut current_grid, pad_amount as i32);
        perform_conway(&current_grid, &mut new_grid, rear_offset, pad_amount, kernel);
        current_grid = new_grid.clone();
    }

    return current_grid.iter().flat_map(|x| x.iter()).sum();
}

fn part2(starting_grid: &Vec<Vec<i32>>, steps: i32) -> i32 {
    let mut current_grid = starting_grid.clone();

    for _ in 0..steps {
        // to make convolution easier, add an extra 0 column to start and end, as well as extra
        // rows at top and bottom
        let mut new_grid = vec![vec![0; current_grid[0].len()]; current_grid.len()];
        let kernel: Vec<Vec<i32>> = vec![vec![1, 1, 1], vec![1, 0, 1], vec![1, 1, 1]];
        let rear_offset = kernel.len() - 1;
        let pad_amount = rear_offset / 2;
        turn_on_corners(&mut current_grid);
        pad_vector(&mut current_grid, pad_amount as i32);
        perform_conway(&current_grid, &mut new_grid, rear_offset, pad_amount, kernel);
        current_grid = new_grid.clone();
    }

    turn_on_corners(&mut current_grid);
    return current_grid.iter().flat_map(|x| x.iter()).sum();
}

pub fn solve(filepath: &String) {
    let input: String = fs::read_to_string(filepath).unwrap();
    let grid = input_to_grid(&input);

    println!("Part 1: {}", part1(&grid, 100));
    println!("Part 2: {}", part2(&grid, 100));
}
