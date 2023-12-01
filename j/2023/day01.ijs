input =: cutLF toJ 1!:1 < '2023/day01.txt'

i =: (('one';'one1one')&stringreplace) &.> input
will =: (('two';'two2two')&stringreplace) &.> i
regret =: (('three';'three3three')&stringreplace) &.> will
this =: (('four';'four4four')&stringreplace) &.> regret
when =: (('five';'five5five')&stringreplace) &.> this
i =: (('six';'six6six')&stringreplace) &.> when
go =: (('seven';'seven7seven')&stringreplace) &.> i
to =: (('eight';'eight8eight')&stringreplace) &.> go
class =: (('nine';'nine9nine')&stringreplace) &.> to
tomorrow =: (('zero';'zero0zero')&stringreplace) &.> class

part1 =: +/ ".> ({.,{:)&.> (] {~ [: I. [: 10&~: '0123456789'&i.)&.>input 
part2 =: +/ ".> ({.,{:)&.> (] {~ [: I. [: 10&~: '0123456789'&i.)&.>tomorrow

part1;part2