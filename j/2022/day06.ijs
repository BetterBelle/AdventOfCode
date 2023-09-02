input =: }: toJ 1!:1 < '2022/day06.txt'

part1 =: 4 + 1 i.~ > (# = [: # ~.)&.> 4<\ input 
part2 =: 14 + 1 i.~ > (# = [: # ~.)&.> 14<\ input

part1;part2