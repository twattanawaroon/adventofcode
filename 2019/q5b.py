import sys
for line in sys.stdin:
    x = list(map(int, line.strip().split(',')))
    inp = 5
    ptr = 0
    paramlen = [0, 2, 2, 0, 1, 2, 2, 2, 2]
    def gett(y, loc, pmode):
        if pmode == 0:
            return y[y[loc]]
        else:
            return y[loc]
    while x[ptr] % 100 != 99:
        cmd = x[ptr] % 100
        details = x[ptr] // 100
        params = []
        for i in range(paramlen[cmd]):
            val = details % 10
            details //= 10
            params.append(val)
        if cmd == 1:
            x[x[ptr+3]] = gett(x, ptr+1, params[0]) + gett(x, ptr+2, params[1])
            ptr += 4
        elif cmd == 2:
            x[x[ptr+3]] = gett(x, ptr+1, params[0]) * gett(x, ptr+2, params[1])
            ptr += 4
        elif cmd == 3:
            x[x[ptr+1]] = inp
            ptr += 2
        elif cmd == 4:
            print(gett(x, ptr+1, params[0]))
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
            x[x[ptr+3]] = 1 if gett(x, ptr+1, params[0]) < gett(x, ptr+2, params[1]) else 0
            ptr += 4
        elif cmd == 8:
            x[x[ptr+3]] = 1 if gett(x, ptr+1, params[0]) == gett(x, ptr+2, params[1]) else 0
            ptr += 4