import sys
import codelib as cl
from aocd import submit

s = set([(0, 0)])
d = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
h = [(0, 0)]*10
for line in sys.stdin:
    x, y = line.strip().split()
    y = int(y)
    dx, dy = d[x]
    for i in range(y):
        hx, hy = h[0]
        h[0] = (hx+dx, hy+dy)
        for j in range(1, 10):
            hx, hy = h[j-1]
            tx, ty = h[j]
            if abs(hx-tx) <= 1 and abs(hy-ty) <= 1:
                continue
            ex = 0 if hx == tx else 1 if hx > tx else -1
            ey = 0 if hy == ty else 1 if hy > ty else -1
            h[j] = (tx+ex, ty+ey)
        s.add(h[9])

ansf = len(s)
#print(ansf)
submit(ansf, part="b", day=9, year=2022)