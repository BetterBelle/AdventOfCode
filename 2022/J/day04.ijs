input =: > ".&.> > '-'cut&.> > ','cut&.> cutLF 1!:1 < '2022/inputs/day04.txt'


part1 =: +/ 1>: +/"1 (0> [: -/ /:~)"2 input
part2 =: +/ >:/"1 (([: {."1 {:"1) ,. ([: {:"1 {."1)) /:~"2 input


part1; part2