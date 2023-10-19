from functools import reduce

with open('data/aoc-2020-03.txt') as f:
    dat = [x.strip() for x in f.readlines()]

def slopecheck(dx, dy):
    width = len(dat[0])
    height = len(dat)

    x = 0
    y = 0

    trees = 0
    while y < height:
        x += dx
        y += dy
        if y >= height:
            return trees
        if dat[y][x % width] == '#':
            trees += 1

    return trees

print('Part 1:', slopecheck(3, 1))

part2 = [slopecheck(1,1), slopecheck(3,1), slopecheck(5,1), slopecheck(7,1), slopecheck(1,2)]
print('Part 2:', reduce(lambda a, b: a*b, part2))
