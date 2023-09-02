input =: 3 | 'ABCXYZ' i. > cutLF (' ';'') stringreplace toJ 1!:1 < '2022/day02.txt'

NB. Could probably figure out how to make this nicer. Function composition/trains are weird
part1 =: ([: +/ [: 1&+ {:"1+ 3* 1+ [: (] - 2&=) [: (] - 2 * 1&=) ([: 3&| -/"1)) input

NB. part1 =: +/ 1&+ {:"1 input + 3&* 1&+ (] - 2&=) (] - [: 2&* 1&=) 3&| -/"1 input
NB. part2 =: +/ (3&* {:"1 input)&+ 1&+ 3&| 1 -~ +/"1 input
part2 =: ([: +/ ([: 3&* {:"1) + [: 1&+ [: 3&| [: _1&+ +/"1) input

part1;part2