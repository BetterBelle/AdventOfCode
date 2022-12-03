input =: <: +: '('= 1!:1 < '2015/inputs/day01.txt'

part1 =: +/ input 

NB. part2 =: {. >: I. _1 = +/\ input
part2 =: >: _1 i.~ +/\ input

part1;part2