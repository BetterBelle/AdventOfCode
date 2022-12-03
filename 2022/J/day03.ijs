input =: (1+~ 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'&i.)&.> cutLF 1!:1 < '2022/inputs/day03.txt'

NB. Probably a better way of doing this considering all the repeating code, but this is good enough
part1 =: +/ , > ([: ~. (] }.~ [: -: #) #~ ([: +./ (] {.~ [: -: #) =/ (] }.~ [: -: #)))&.> input

NB. This language is insane
part2 =: +/ >./"1 +./"2 (1&{ #~ 1&{ =/~ [: ~. {: #~ [: +./ {. =/ {:)"2 > _3]\ input

part1;part2