use std::{fs, cmp};

#[derive(Debug)]
struct Ingredient {
    capacity : i64,
    durability : i64,
    flavor : i64,
    texture : i64,
    calories : i64,
}

impl Ingredient {
    pub fn new(capacity : i64, durability : i64, flavor : i64, texture : i64, calories : i64) -> Ingredient {
        return Ingredient { capacity, durability, flavor, texture, calories };
    }
}

#[derive(Debug)]
struct Recipe {
    ingredients : Vec<Ingredient>,
}

impl Recipe {
    pub fn new(ingredients : Vec<Ingredient>) -> Recipe {
        return Recipe { ingredients };
    }

    pub fn maximize_score(&self, teaspoon_restriction : i64, calorie_restriction : i64) -> i64 {
        let mut max_score : i64 = 0;
        for a in 0..teaspoon_restriction + 1 {
            for b in 0..teaspoon_restriction + 1 - a {
                for c in 0..teaspoon_restriction + 1 - a - b {
                    let d : i64 = teaspoon_restriction - a - b - c;
                    let capacity : i64 = a*self.ingredients[0].capacity + b*self.ingredients[1].capacity + c*self.ingredients[2].capacity + d*self.ingredients[3].capacity;
                    let durability : i64 = a*self.ingredients[0].durability + b*self.ingredients[1].durability + c*self.ingredients[2].durability + d*self.ingredients[3].durability;
                    let flavor : i64 = a*self.ingredients[0].flavor + b*self.ingredients[1].flavor + c*self.ingredients[2].flavor + d*self.ingredients[3].flavor;
                    let texture : i64 = a*self.ingredients[0].texture + b*self.ingredients[1].texture + c*self.ingredients[2].texture + d*self.ingredients[3].texture;
                    let calories : i64 = a*self.ingredients[0].calories + b*self.ingredients[1].calories + c*self.ingredients[2].calories + d*self.ingredients[3].calories;
                    if capacity >= 0 && durability >= 0 && flavor >= 0 && texture >= 0 {
                        if calorie_restriction < 0 {
                            max_score = cmp::max(capacity * durability * flavor * texture, max_score);
                        }
                        else if calorie_restriction == calories {
                            max_score = cmp::max(capacity * durability * flavor * texture, max_score);
                        }
                    }
                }
            }
        }

        return max_score;
    }
}

fn create_recipe(input : String) -> Recipe {
    let number_matcher: regex::Regex = regex::Regex::new(r"-?[0-9]+").unwrap();
    let matches: Vec<regex::Match<'_>> = number_matcher.find_iter(&input).collect();
    let matched: Vec<i64> = matches.iter().map(|x: &regex::Match<'_>| x.as_str().parse::<i64>().unwrap()).collect();
    let mut ingredients : Vec<Ingredient> = Vec::new();
    for i in (0..matched.len()/5).into_iter().map(|x| x * 5) {
        ingredients.push(Ingredient::new(matched[i], matched[i+1], matched[i+2], matched[i+3], matched[i+4]));
    }
    return Recipe::new(ingredients);
}

fn part1(recipe : &Recipe) -> i64 {
    return recipe.maximize_score(100, -1);
}

fn part2(recipe : &Recipe) -> i64 {
    return recipe.maximize_score(100, 500);
}

pub fn solve(filepath: &String) {
    let input: String = fs::read_to_string(filepath).unwrap();
    let recipe: Recipe = create_recipe(input);
    println!("{:?}", recipe);

    println!("Part 1: {}", part1(&recipe));
    println!("Part 2: {}", part2(&recipe));
}
