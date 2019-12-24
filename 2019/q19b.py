import sys
from collections import deque

def attempt(x, inp):
    ptr = 0
    relbase = 0
    paramlen = [0, 3, 3, 1, 1, 2, 2, 3, 3, 1]
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
            inpv = inp.pop(0)
            sett(x, ptr+1, params[0], inpv)
            ptr += 2
        elif cmd == 4:
            output = gett(x, ptr+1, params[0])
            ptr += 2
            return output
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

for line in sys.stdin:
    x = list(map(int, line.strip().split(',')))
    bounds = dict()
    i = 5
    a = 10000
    b = -10000
    for j in range(50):
        if attempt(x[:], [i, j]) == 1:
            a = min(a, j)
            b = max(b, j)
    bounds[i] = (a, b)
    while not (i-99 in bounds and a+99 <= bounds[i-99][1]):
        i += 1
        while attempt(x[:], [i, a]) == 0:
            a += 1
        while attempt(x[:], [i, b+1]) == 1:
            b += 1
        bounds[i] = (a,b)
    ansi = i-99
    ansj = a
    print(ansi*10000+ansj)