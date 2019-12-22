import sys
from itertools import permutations

def compute(x, inputs, ptr):
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
            if len(inputs) <= 0:
                return None
            x[x[ptr+1]] = inputs[0]
            inputs.pop(0)
            ptr += 2
        elif cmd == 4:
            return (gett(x, ptr+1, params[0]), ptr+2)
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
    return None

for line in sys.stdin:
    best = None
    x = list(map(int, line.strip().split(',')))
    
    for seq in permutations(list(range(5, 10))):
        machines = []
        inputs = []
        ptrs = []
        for i in range(5):
            machines.append(x[:])
            inputs.append([])
            ptrs.append(0)
        for i in range(5):
            inputs[i].append(seq[i])
        val = 0
        fail = False
        while not fail:
            bval = val
            for i in range(5):
                inputs[i].append(val)
                res = compute(machines[i], inputs[i], ptrs[i])
                if res is None:
                    fail = True
                    break
                else:
                    val, newptr = res
                    ptrs[i] = newptr
        if best is None or best < bval:
            best = bval
    print(best)