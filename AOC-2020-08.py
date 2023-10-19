with open('data/aoc-2020-08.txt') as f:
    dat = [x.strip().split(' ') for x in f.readlines()]

def runprg(swap=-1):
    pcTgt = len(dat)
    acc = 0
    pc = 0
    visited = set()

    while True:
        if pc in visited:
            return (False, acc)
        if pc == pcTgt:
            return (True, acc)

        instr = dat[pc]
        visited.add(pc)
        
        if instr[0] == 'acc':
            acc += int(instr[1].lstrip('+'))
            pc += 1
        elif instr[0] == 'nop' and not pc == swap or instr[0] == 'jmp' and pc == swap:
            pc += 1
        elif instr[0] == 'jmp' and not pc == swap or instr[0] == 'nop' and pc == swap:
            pc += int(instr[1].lstrip('+'))


print('Part 1:', runprg()[1])

for i, d in enumerate(dat):
    if d[0] == 'acc':
        continue
    term, acc = runprg(i)
    if term:
        print('Part 2:', acc)
        break
