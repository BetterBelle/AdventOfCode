input =: 1!:1 < '2015/inputs/day02.txt'

NB. Creates lists of sizes
sizes =: ".&>'x'cut&>cutLF input

part1 =: +/ , ([: (+: , {.) ([: (2 */\ (, {.)) /:~))"1 sizes

part2 =: +/ ([: +/ [: (*/ ,~ [: +: }:) /:~)"1 sizes

part1;part2
