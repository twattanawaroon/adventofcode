import sys

painted = dict()
global odd
global xx
global yy
global dd
odd = True
xx = 0
yy = 0
dd = 0
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
painted[(0,0)] = 1

def output(step):
    global odd
    global xx
    global yy
    global dd
    if odd:
        painted[(xx,yy)] = step
    else:
        dd = (dd+(1 if step == 1 else 3))%4
        xx += dirs[dd][0]
        yy += dirs[dd][1]
    odd = not odd

def get_input():
    if (xx,yy) in painted:
        return painted[(xx,yy)]
    else:
        return 0

for line in sys.stdin:
    x = list(map(int, line.strip().split(',')))
    inp = 2
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
            inp = get_input()
            sett(x, ptr+1, params[0], inp)
            ptr += 2
        elif cmd == 4:
            output(gett(x, ptr+1, params[0]))
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

paintedx = [x for (x,y) in painted]
paintedy = [y for (x,y) in painted]
mx = min(paintedx)
my = min(paintedy)
px = max(paintedx)
py = max(paintedy)
board = []
for i in range(px-mx+1):
    board.append([0]*(py-my+1))
for (x,y) in painted:
    board[x-mx][y-my] = painted[(x,y)]
print(len(painted))
for line in board:
    print(''.join(map(lambda x: '#' if x == 1 else ' ', line)))