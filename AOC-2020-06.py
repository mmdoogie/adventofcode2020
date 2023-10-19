with open('data/aoc-2020-06.txt') as f:
    dat = [x.strip() for x in f.readlines()]

def part1():
    ans = []

    grp = set()
    for line in dat:
        if line == '':
            ans += [len(grp)]
            grp = set()
            continue
        for ch in line:
            grp.add(ch)
    ans += [len(grp)]

    return sum(ans)

def part2():
    cnt = 0

    grp = []
    for line in dat:
        if line == '':
            cnt += sum([all([q in l for l in grp]) for q in 'abcdefghijklmnopqrstuvwxyz'])
            grp = []
            continue
        grp += [line]
    cnt += sum([all([q in l for l in grp]) for q in 'abcdefghijklmnopqrstuvwxyz'])

    return cnt

print('Part 1:', part1())
print('Part 2:', part2())
