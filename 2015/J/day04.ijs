NB. Need to include the md5 addon
load '~addons/convert/misc/md5.ijs'
input =: 1!:1 < '2015/inputs/day04.txt'

Note 'creating the inputs'
    i. 5000000  Creates the numbers from 0 to 5000000 for appending to the input
    > ;/        Converts everything to cells
    &.          Applies the left to each element in the right box
    input,":    Catenates the stringified version of the numbers to the right of the input
)
search =: (input,":) &. > ;/ i. 5000000
Note 'hashing (warning: VERY SLOW)'
    md5 &> A    Applies the md5 hash to every element that we are searching for
)
hashes =: md5 &> search

Note 'part 1 and 2 in one line'
    _ 5&{.          grabs the first 5 of each hash
    '0...' -:"1     runs a match, creating a mask of which ones have the first few 0s
    #~              Because this gets run as hashes #~ matches from hooks,
                    It actually does matches # hashes, which returns the matching hashes
    i.              Gives the indexes of the matches
    {.              Head i.e. first match
)
] part1 =: {. (i. (#~ ('00000' (-:"1) _ 5&{.))) hashes
] part2 =: {. (i. (#~ ('000000' (-:"1) _ 6&{.))) hashes