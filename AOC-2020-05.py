import itertools

with open('data/aoc-2020-05.txt') as f:
    dat = [x.strip() for x in f.readlines()]

def seatid(item):
    minRow = 0
    maxRow = 127

    for c in item[0:7]:
        span = maxRow - minRow + 1
        if c == 'F':
            maxRow -= span/2
        if c == 'B':
            minRow += span/2

    minCol = 0
    maxCol = 7
    for c in item[7:]:
        span = maxCol - minCol + 1
        if c == 'L':
            maxCol -= span/2
        if c == 'R':
            minCol += span/2

    return int(minRow * 8 + minCol)

ids = [seatid(i) for i in dat]
print('Part 1:', max(ids))

def myseat(ids):
    for a,b in itertools.pairwise(sorted(ids)):
        if b-a > 1:
            return a+1

print('Part 2:', myseat(ids))
