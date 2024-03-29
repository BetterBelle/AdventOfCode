input =: 1!:1 < '2015/day03.txt'

Note 'Part 1 in one chain'
    '^>v<' i.   This part turns the four symbols into 0 1 2 3 on matching
    (0j1(^i.)4) This is the four powers of i, starting with 0
                Explanation:
                    (^i.)4: i.4 gives 0 1 2 3, with the ^ gives you 4 ^ 0 1 2 3
                    0j1   : this turns 4 ^ 0 1 2 3 to 0j1 ^ 0 1 2 3, giving you the four rotations 1 0j1 _1 0j_1
    {~          This maps each of the 0 1 2 3 from the input into one of the four rotations on index
    0 ,         Append a 0 because you start at 0
    +/\         Running sum
    ~.          Nub, i.e. remove duplicates, leaving only houses that have been visited at least once
    #           Count
)
part1 =: # ~. +/\ 0 , (0j1(^i.)4) {~ '^>v<' i. input

part2 =:  # ~. , +/\ 0 , ((0j1(^i.)4) {~ '^>v<'&i. $~ 2 ,~ [: -: #) input

part1;part2