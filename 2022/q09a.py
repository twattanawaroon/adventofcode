import sys
import codelib as cl
from aocd import submit

s = set([(0, 0)])
d = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
hx = 0
hy = 0
tx = 0
ty = 0
for line in sys.stdin:
    x, y = line.strip().split()
    y = int(y)
    dx, dy = d[x]
    for i in range(y):
        hx += dx
        hy += dy
        if abs(hx-tx) <= 1 and abs(hy-ty) <= 1:
            continue
        ex = 0 if hx == tx else 1 if hx > tx else -1
        ey = 0 if hy == ty else 1 if hy > ty else -1
        tx += ex
        ty += ey
        #print((tx, ty))
        s.add((tx, ty))

ansf = len(s)
#print(ansf)
submit(ansf, part="a", day=9, year=2022)