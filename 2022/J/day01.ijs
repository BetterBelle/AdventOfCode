input =: ". > cutLF ('  ';LF) stringreplace (LF;' ') stringreplace 1!:1 < '2022/inputs/day01.txt'

part1 =: {: /:~ +/"1 input
part2 =: +/ 3 {. \:~ +/"1 input

NB. part1 =: >./ +/"1 input
NB. part1 =: {. \:~ +/"1 input

NB. part2 =: +/ {: 3]\ /:~ +/"1 input
NB. part2 =: +/ {. 3]\ \:~ +/"1 input
NB. part2 =: +/ ((3-~ #) }. ([: /:~ +/"1)) input

part1;part2