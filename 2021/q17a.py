import sys
import codelib as cl

def parse_range(s):
    return tuple(map(int,s.split('..')))

def in_target(x, y, minx, maxx, miny, maxy):
    return minx <= x <= maxx and miny <= y <= maxy

def eventual(ux, uy, minx, maxx, miny, maxy):
    x = 0
    y = 0
    vx = ux
    vy = uy
    hy = None
    while x <= maxx and y >= miny:
        x += vx
        y += vy
        hy = max(y, hy) if hy is not None else y
        vx += 1 if vx < 0 else 0 if vx == 0 else -1
        vy -= 1
        if in_target(x, y, minx, maxx, miny, maxy):
            return hy
    return None

for line in sys.stdin:
    s = line.strip().split()
    minx, maxx = parse_range(s[2][2:-1])
    miny, maxy = parse_range(s[3][2:])

ans = []
for uy in range(miny,abs(miny)):
    for ux in range(1,maxx+1):
        p = eventual(ux, uy, minx, maxx, miny, maxy)
        if p is not None:
            ans.append(p)

print(max(ans))
