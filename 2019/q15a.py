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
            sett(x, ptr+1, params[0], inp)
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

def inbound(px, py):
    MX = 100
    return -MX <= px <= MX and -MX <= py <= MX

def opposite(pn):
    return (0,2,1,4,3)[pn]

def dfs(x, g, px, py):
    dirs = ((1,-1,0),(2,1,0),(3,0,-1),(4,0,1))
    for dn, dx, dy in dirs:
        if inbound(px+dx, py+dy) and (px+dx, py+dy) not in g:
            res = attempt(x, dn)
            if res == 0:
                g[(px+dx, py+dy)] = '#'
            elif res == 1:
                g[(px+dx, py+dy)] = '.'
                dfs(x, g, px+dx, py+dy)
                attempt(x, opposite(dn))
            elif res == 2:
                g[(px+dx, py+dy)] = 'Y'
                dfs(x, g, px+dx, py+dy)
                attempt(x, opposite(dn))
            else:
                g[(px+dx, py+dy)] = '?'
                dfs(x, g, px+dx, py+dy)
                attempt(x, opposite(dn))

def bfs(g):
    q = deque()
    q.append((0,0))
    dist = dict()
    dist[(0,0)] = 0
    dirs = ((1,-1,0),(2,1,0),(3,0,-1),(4,0,1))
    while len(q) > 0:
        px, py = q.popleft()
        if g[(px,py)] == 'Y':
            return dist[(px, py)]
        for dn, dx, dy in dirs:
            if (px+dx, py+dy) not in dist and g[(px+dx, py+dy)] != '#':
                dist[(px+dx, py+dy)] = dist[(px, py)]+1
                q.append((px+dx, py+dy))
    return None

for line in sys.stdin:
    x = list(map(int, line.strip().split(',')))
    MX = 100
    m = dict()
    m[(0,0)] = '.'
    dfs(x[:], m, 0, 0)
    print(bfs(m))