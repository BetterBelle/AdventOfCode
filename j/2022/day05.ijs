NB. These are the stacks, I hard code these because I can't be asked to parse through them properly
NB. [N] [G]                     [Q]    
NB. [H] [B]         [B] [R]     [H]    
NB. [S] [N]     [Q] [M] [T]     [Z]    
NB. [J] [T]     [R] [V] [H]     [R] [S]
NB. [F] [Q]     [W] [T] [V] [J] [V] [M]
NB. [W] [P] [V] [S] [F] [B] [Q] [J] [H]
NB. [T] [R] [Q] [B] [D] [D] [B] [N] [N]
NB. [D] [H] [L] [N] [N] [M] [D] [D] [B]
NB.  1   2   3   4   5   6   7   8   9 

stacks =: 'dtwfjshn';'hrpqtnbg';'lqv';'nbswrq';'ndftvmb';'mdbvhtr';'dbqj';'dnjvrzhq';'bnhms'

NB. stacks =: (1{.stacks) , (<'stop'), (2 }. stacks)

input =: > (0 1 1 -~ ])&.> ([: (0&~: # ]) 0&".)&.> cutLF toJ 1!:1 < '2022/day05.txt'
{. input

]stacks =: (((> stacks {~ 2&{&{. input),(|.(-0&{&{. input) {. > stacks {~ 1&{&{. input)); < (([: > stacks {~ 1&{&{.) }.~ ([: - 0&{&{.)) input) ((2&{ , 1&{) {. input)} stacks
NB. ]stacks =: (< (> (2 { {. input) { stacks),((- (0 { {. input)) {. > (1 { {. input) { stacks)) (2 { {. input) } stacks
