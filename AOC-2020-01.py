from itertools import permutations
from functools import reduce

with open('data/aoc-2020-01.txt') as f:
    dat = [int(x.strip()) for x in f.readlines()]

def doit(cnt):
    for p in permutations(dat, cnt):
        if sum(p) == 2020:
            return reduce(lambda a, b: a*b, p)

print('Part 1:', doit(2))
print('Part 2:', doit(3))

