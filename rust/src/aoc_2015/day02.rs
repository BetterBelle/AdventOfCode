use std::fs;

struct Dimensions {
    l: i32,
    w: i32,
    h: i32
}

fn part1(input: &Vec<Dimensions>) -> i32 {
    let mut total_area: i32 = 0;
    for order in input {
        let areas: [i32; 3] = [order.l * order.w, order.w * order.h, order.l * order.h];
        let min_area: i32 = *areas.iter().min().expect("Something went horribly wrong");
        let doubled_areas: i32 = areas.map(|x: i32| 2 * x).into_iter().sum();
        total_area += min_area + doubled_areas;
    }

    return total_area;
}

fn part2(input: &Vec<Dimensions>) -> i32 {
    let mut total_area: i32 = 0;
    for order in input {
        let mut temp: [i32; 3] = [order.l, order.w, order.h];
        temp.sort();
        total_area += 2 * temp[0] + 2 * temp[1] + (temp[0] * temp[1] * temp[2]);
    }

    return total_area;
}

pub fn solve(filepath: &String) {
    let file_contents: String = fs::read_to_string(filepath).unwrap();

    let mut input: Vec<Dimensions> = Vec::new();
    for dims in file_contents.lines() {
        let mut collector: std::str::Split<'_, char> = dims.split('x');
        let new_item: Dimensions = Dimensions {
            l: collector.next().unwrap().parse::<i32>().unwrap(),
            w: collector.next().unwrap().parse::<i32>().unwrap(),
            h: collector.next().unwrap().parse::<i32>().unwrap()
        };
        input.push(new_item);
    }
    
    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}