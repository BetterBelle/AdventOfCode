input =: > ".&.> > '-'cut&.> > ','cut&.> cutLF toJ 1!:1 < '2022/day04.txt'


part1 =: +/ 1>: +/"1 (0> [: -/ /:~)"2 input
part2 =: +/ >:/"1 (([: {."1 {:"1) ,. ([: {:"1 {."1)) /:~"2 input


part1; part2