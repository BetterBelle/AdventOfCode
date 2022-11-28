input =: 1!:1 < '2015/inputs/day01.txt'

Note 'parsing input'
    '('=input boolean mask for ( 
    +: double to create 2s and 0s
    <: decrement for -1 and 1 indicating going up or down a floor
)
levels =: <: +: '('=input 

Note 'sum of all for last level'
    +/ levels is just reduce add
)
] part1 =: +/ levels 

Note 'part 2'
    +/\ reduce add on all sublists of levels
    _1 = boolean mask where we reach the basement
    I. indexes of where we reached the basement
    >: increment that because we want position (+1 of index)
    {. is head (i.e. first element) to give us the first time we reach the basement
)
] part2 =: {. >: I. _1 = +/\ levels