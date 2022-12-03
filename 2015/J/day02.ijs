input =: 1!:1 < '2015/inputs/day02.txt'

NB. Creates lists of sizes
sizes =: ".&>'x'cut&>cutLF input

Note 'Part 1 as one chain'
    Part 1 requires you to get the area of each box plus the area of the smallest side, then summing all of these results
    /:~"1               Sort each sublist of sizes
                        Creates a bunch of lists h w l, where h < w < l
    (2 */\ (, {.))"1    Append the smallest item (head) of each list
                        On each of these, apply */ on each sublist of size 2
                        This effectively creates lists h w l h -> h*w w*l l*h
    (+: , {.)"1         On each list, append the head (smallest side) to the double of each
                        This effectively goes from h*w w*l l*h -> 2*h*w 2*w*l 2*l*h h*w
    +/ +/               Sum everything
)
part1 =: +/ +/ (+: , {.)"1 (2 */\ (, {.))"1 /:~"1 sizes

Note 'Part 2 as one chain'
    Part 2 requires you to get the cubic feet of volume of each, plus the shortest perimeter (smallest 2 sides doubled and summed)
    /:~"1                   Sort each sublist of sizes
    ((+: @ }:) , */)"1      Big explanation:
                            (+: @ }:) is double(curtail(input)) This gives the two smallest sides doubled
                            */ is simply the cubic volume (*/ on input)
                            , catenates the two together because of how function trains work in J
    +/ +/                   sum everything
)
part2 =: +/ +/ ((+: @ }:) , */)"1 /:~"1 sizes

part1;part2
