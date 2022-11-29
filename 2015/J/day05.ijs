input =: 1!:1 < '2015/inputs/day05.txt'
strings =: cutLF input

Note 'Part 1 in one chain'
    > +./&.> 2=/\&.> strings                                                        
        Whether the string has a substring of length 2 where both are identical
        2=/\&.>     Creates every overlapping pair then checks if the pairs are two identical tokens and creates a mask
        +./&.>      Goes through each mask and runs an or, meaning if a string has a substring where the two chars are
                    the same, that string will be a 1
        >           The result is a bunch of boxes, this unboxes, leaving us with the list of 1s and 0s

    ,. stitch

    3 <: +/"1 +/"2 =/"1 (;/'aeiou') ,"0"1 0 (> ;/&.> strings)                       
        Whether a string has at least 3 vowels
        > ;/&.>     Creates a bunch of box lists of each letter from the strings
        ,"0"1 0     Creates a pairwise matching (like a cross product) of boxed characters
                    Creates these for every single string
        =/"1        Creates a mask of size left argument (aeiou) for if the pairs are equal, for every letter in each word
        +/"2        Sums the mask per letter, counting the occurences of each vowel per word
        +/"1        For every word sum up the total amount of vowels, creating a list of vowel counts per word
        3 <:        Creates a mask, each word where the count of vowels is 3 or greater to be 1

    ,. stitch

    -. +./"1 +./"2 =/"1 (;/ 4 2 $ 'abcdpqxy') ,"0"1 0 (> ;/&.> (2]\&.> strings))  
        True if doesn't contain bad pair
        2]/^.>      Creates every length 2 substring of the strings
        ;/&.>       Boxes each substring into it's own box
        >           Unbox one level, leaving us with lists of boxed pairs
        ,"0"1 0     As above, creates pairwise matchings of boxes
                    Creates these for every string we don't want to see
        ;/ 4 2 $    Creates the boxes for each pair we don't want to see to pairwise match because of above
        =/"1        Creates a mask of size left argument (in our case 4 for the number of pairs we don't want)
                        for if the substring is the same as the left argument for each pair in each word
                    Basically, this creates a bunch of 2d lists, each 2d list being 4xlength of word, each list length 4 being a mask
                        of whether that particular substring we don't want is in the word
        +./"2       Bitwise or on each pair of every word, to check if a particular substring has been spotted
                    Leaves us with a bunch of length 4 lists, one for each word, with 1s for if that particular pair is in the word
        +./"1       Again an or on each word, this time to tell us whether that word is naughty, because if there's a 1 at all,
                        that means that word contains a bad pair
        -.          Not everything. This leaves us with a 1 on good words, 0 for naughty word

    *./"1           Perform an and on each triple, telling us if that word is nice (1) or not (0)
    Result is a list of 1s and 0s, 1s being nice strings, 0 being naughty strings

    +/ then just gives you the number of nice strings
)

]part1 =: +/ *./"1 (> +./&.> 2=/\&.> strings) ,. (3<: +/"1 +/"2 =/"1 (;/'aeiou') ,"0"1 0 (> ;/&.> strings)) ,. (-. +./"1 +./"2 =/"1 (;/ 4 2 $ 'abcdpqxy') ,"0"1 0 (> ;/&.> (2]\&.> strings)))

]part2 =: strings