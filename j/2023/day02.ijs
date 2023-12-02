input =: cutLF toJ 1!:1 < '2023/day02.txt'
bounds =: 12 13 14

parsed_input =: |: >./"1 ".@('[0-9]+'&rxfirst&>)&>@(('[0-9]+ red'&rxall);('[0-9]+ green'&rxall);<@('[0-9]+ blue'&rxall))&> input
part1 =: +/ >: I. <./ bounds&>: parsed_input
part2 =: +/ */ parsed_input

part1;part2