import sys
from collections import deque

def attempt(x, inp):
    ptr = 0
    relbase = 0
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
            if len(inp) > 0:
                inpv = inp.pop(0)
                sett(x, ptr+1, params[0], inpv)
                ptr += 2
            else:
                return x, output, False
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
    return x, output, True

for line in sys.stdin:
    x = list(map(int, line.strip().split(',')))
    x[0] = 2
    grid = dict()
    maxx = 0
    maxy = 0
    done = False
    ina = []
    step = 0
    while not done and step <= 10**4:
        x, out, done = attempt(x, ina)
        for i in range(len(out)//3):
            xx, yy, zz = out[i*3:(i+1)*3]
            grid[(xx, yy)] = zz
            if zz == 3:
                padx = xx
            elif zz == 4:
                ballx = xx
            maxx = max(maxx, xx)
            maxy = max(maxy, yy)
        if ballx < padx:
            zin = -1
        elif ballx > padx:
            zin = 1
        else:
            zin = 0
        ina.append(zin)
        step += 1
    print(step)
    print(grid[(-1,0)])
    for yy in range(maxy+1):
        scr = []
        for xx in range(maxx+1):
            if (xx,yy) not in grid:
                scr.append(' ')
            elif grid[(xx,yy)] == 0:
                scr.append('.')
            elif grid[(xx,yy)] == 1:
                scr.append('#')
            elif grid[(xx,yy)] == 2:
                scr.append('X')
            elif grid[(xx,yy)] == 3:
                scr.append('-')
            elif grid[(xx,yy)] == 4:
                scr.append('o')
        print(''.join(scr))