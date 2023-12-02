input =: cutLF toJ 1!:1 < '2023/day01.txt'
replace =: [: ('one';'one1one')&stringreplace [: ('two';'two2two')&stringreplace [: ('three';'three3three')&stringreplace [: ('four';'four4four')&stringreplace [: ('five';'five5five')&stringreplace [: ('six';'six6six')&stringreplace [: ('seven';'seven7seven')&stringreplace [: ('eight';'eight8eight')&stringreplace [: ('nine';'nine9nine')&stringreplace ('zero';'zero0zero')&stringreplace


part1 =: +/ ". ({. , {:)&> ({~ [: I. [: 10&~: '0123456789'&i.)&.>input 
part2 =: +/ ". ({. , {:)&> ({~ [: I. [: 10&~: '0123456789'&i.)&.> replace&.> input

part1;part2