import sys
from collections import deque

def attempt(x, inp, ptr, relbase):
    paramlen = [0, 3, 3, 1, 1, 2, 2, 3, 3, 1]
    output = []
    def gett(y, loc, pmode):
        if pmode == 0:
            pos = y[loc]
        elif pmode == 1:
            return y[loc]
        else:
            pos = y[loc]+relbase
        if pos >= len(y):
            y.extend([0] * (pos-len(y)+1))
        return y[pos]
    def sett(y, loc, pmode, val):
        if pmode == 0:
            pos = y[loc]
        else:
            pos = y[loc]+relbase
        if pos >= len(y):
            y.extend([0] * (pos-len(y)+1))
        y[pos] = val
    while x[ptr] % 100 != 99:
        cmd = x[ptr] % 100
        details = x[ptr] // 100
        params = []
        for i in range(paramlen[cmd]):
            val = details % 10
            details //= 10
            params.append(val)
        if cmd == 1:
            r = gett(x, ptr+1, params[0]) + gett(x, ptr+2, params[1])
            sett(x, ptr+3, params[2], r)
            ptr += 4
        elif cmd == 2:
            r = gett(x, ptr+1, params[0]) * gett(x, ptr+2, params[1])
            sett(x, ptr+3, params[2], r)
            ptr += 4
        elif cmd == 3:
            if len(inp) == 0:
                return output, False, ptr, relbase
            else:
                inpv = inp.pop(0)
                sett(x, ptr+1, params[0], inpv)
                ptr += 2
        elif cmd == 4:
            output.append(gett(x, ptr+1, params[0]))
            ptr += 2
        elif cmd == 5:
            if gett(x, ptr+1, params[0]) != 0:
                ptr = gett(x, ptr+2, params[1])
            else:
                ptr += 3
        elif cmd == 6:
            if gett(x, ptr+1, params[0]) == 0:
                ptr = gett(x, ptr+2, params[1])
            else:
                ptr += 3
        elif cmd == 7:
            r = 1 if gett(x, ptr+1, params[0]) < gett(x, ptr+2, params[1]) else 0
            sett(x, ptr+3, params[2], r)
            ptr += 4
        elif cmd == 8:
            r = 1 if gett(x, ptr+1, params[0]) == gett(x, ptr+2, params[1]) else 0
            sett(x, ptr+3, params[2], r)
            ptr += 4
        elif cmd == 9:
            relbase += gett(x, ptr+1, params[0])
            ptr += 2
    return output, True, ptr, relbase

cmds = 'ETNTWSTNNWTESESENTSEEETWWWWWNTNNTE'
items = ['whirled peas', 'coin', 'antenna', 'astrolabe', 'prime number', 'dark matter', 'fixed point', 'weather machine']
translate = {
    'N': 'north',
    'S': 'south',
    'W': 'west',
    'E': 'east',
    'T': 'take',
}
xmds = []
kmap = [True]*8
while any(kmap):
    for i in range(8):
        if kmap[i]:
            # drop i
            xmds.append('drop '+items[i])
            kmap[i] = False
            break
        else:
            # pick i
            xmds.append('take '+items[i])
            kmap[i] = True
    xmds.append('inv')
    xmds.append('south')

for line in open('input25.txt', 'r'):
    x = list(map(int, line.strip().split(',')))
    done = False
    ptr = 0
    rlb = 0
    oup, done, ptr, rlb = attempt(x, [], ptr, rlb)
    print(''.join(map(chr,oup[:-1])))
    item_count = 0
    for cmd in cmds:
        raw = translate[cmd]
        if cmd == 'T':
            raw += ' ' + items[item_count]
            item_count += 1
        inp = list(map(ord,raw))
        inp.append(ord('\n'))
        oup, done, ptr, rlb = attempt(x, inp, ptr, rlb)
        print(''.join(map(chr,oup[:-1])))
    for xmd in xmds:
        inp = list(map(ord,xmd))
        inp.append(ord('\n'))
        oup, done, ptr, rlb = attempt(x, inp, ptr, rlb)
        print(''.join(map(chr,oup[:-1])))
        if done:
            break
    # Manual part, no longer used
    '''while not done:
        raw = input().strip()
        inp = list(map(ord,raw))
        inp.append(ord('\n'))
        oup, done, ptr, rlb = attempt(x, inp, ptr, rlb)
        print(''.join(map(chr,oup[:-1])))'''