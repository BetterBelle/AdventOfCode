use std::fs;

pub fn part1(input: &Vec<[i32; 3]>) -> i32 {
    let mut total_area: i32 = 0;
    for order in input {
        let areas: [i32; 3] = [order[0] * order[1], order[1] * order[2], order[0] * order[2]];
        let min_area: i32 = *areas.iter().min().expect("Something went horribly wrong");
        let doubled_areas: i32 = areas.map(|x: i32| 2 * x).into_iter().sum();
        total_area += min_area + doubled_areas;
    }

    return total_area;
}

pub fn part2(input: &Vec<[i32; 3]>) -> i32 {
    let mut total_area: i32 = 0;
    for order in input {
        let mut temp: [i32; 3] = [order[0], order[1], order[2]];
        temp.sort();
        total_area += 2 * temp[0] + 2 * temp[1] + (temp[0] * temp[1] * temp[2]);
    }

    return total_area;
}

pub fn solve(filepath: &String) {
    let file_contents: String = fs::read_to_string(filepath)
        .expect("Should have read the file.");

    let mut input: Vec<[i32; 3]> = Vec::new();
    for dims in file_contents.lines() {
        let mut collector: std::str::Split<'_, char> = dims.split('x');
        let new_item: [i32; 3] = [
            collector.next().unwrap().parse::<i32>().unwrap(),
            collector.next().unwrap().parse::<i32>().unwrap(),
            collector.next().unwrap().parse::<i32>().unwrap()
            ];
        input.push(new_item);
        dbg!("{}", new_item);
    }
    
    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}