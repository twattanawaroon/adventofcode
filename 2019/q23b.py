import sys
from collections import deque

def step(x, inp, oup, ptr, relbase, idle):
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
    if x[ptr] % 100 != 99:
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
                idle = False
                inpv = inp.pop(0)
            else:
                idle = True
                inpv = -1
            sett(x, ptr+1, params[0], inpv)
            ptr += 2
        elif cmd == 4:
            idle = False
            oup.append(gett(x, ptr+1, params[0]))
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
    return ptr, relbase, idle

for line in sys.stdin:
    x_base = list(map(int, line.strip().split(',')))
    x = []
    inp = []
    oup = []
    ptr = []
    rlb = []
    idl = []
    for i in range(50):
        x.append(x_base[:])
        inp.append([i])
        oup.append([])
        ptr.append(0)
        rlb.append(0)
        idl.append(False)
    done = False
    cnt = 0
    lasty = None
    while not done:
        for i in range(50):
            ptr_n, rlb_n, idl_n = step(x[i], inp[i], oup[i], ptr[i], rlb[i],idl[i])
            ptr[i] = ptr_n
            rlb[i] = rlb_n
            idl[i] = idl_n
            while len(oup[i]) >= 3:
                pd = oup[i].pop(0)
                px = oup[i].pop(0)
                py = oup[i].pop(0)
                if pd == 255:
                    natx = px
                    naty = py
                else:
                    inp[pd].append(px)
                    inp[pd].append(py)
        all_idle = all([idl[i] for i in range(50)])
        if all_idle:
            cnt += 1
        else:
            cnt = 0
        if cnt >= 100:
            cnt = 0
            if naty == lasty:
                print(naty)
                done = True
            inp[0].append(natx)
            inp[0].append(naty)
            lasty = naty