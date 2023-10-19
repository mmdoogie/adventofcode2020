from itertools import combinations

with open('data/aoc-2020-09.txt') as f:
    dat = [int(x.strip()) for x in f.readlines()]

def part1():
    for i, d in enumerate(dat):
        if i < 25:
            continue

        if sum([dat[i-25+a] + dat[i-25+b] == d for a, b in combinations(range(25), 2)]) == 0:
            return d

p1v = part1()
print('Part 1:', p1v)

def part2():
    for a,b in combinations(range(len(dat)), 2):
        if sum(dat[a:b]) == p1v:
            return min(dat[a:b]) + max(dat[a:b])

print('Part 2:', part2())
