a =: ' ', , a. {~ 97 65 +/ i. 26
input =: a&i.&.> cutLF toJ 1!:1 < '2022/inputs/day03.txt'

inputv2 =: cutLF toJ 1!:1 < '2022/inputs/day03.txt'

NB. Probably a better way of doing this considering all the repeating code, but this is good enough
NB. part1 =: +/ , > ([: ~. (] }.~ [: -: #) #~ ([: +./ (] {.~ [: -: #) =/ (] }.~ [: -: #)))&.> input
part1 =: +/ a i. (~.@(e. # [)/@$~ 2 , -:@#)@> inputv2

NB. This language is insane
NB. part2 =: +/ >./"1 ([: +./ 1&{ #~ 1&{ =/~ [: ~. {: #~ [: +./ {. =/ {:)"2 > _3]\ input
part2 =: +/ , a i. _3 ~.@(e. # [)/\&:> inputv2

part1;part2