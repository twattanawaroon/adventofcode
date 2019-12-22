import sys

def counter(l):
    d = dict()
    for c in l:
        p = int(c)
        if p not in d:
            d[p] = 0
        d[p] += 1
    return d

best = None
bestd = None
for line in sys.stdin:
    x = line.strip()
    for s in range(0, len(x), 150):
        y = x[s:s+150]
        d = counter(y)
        if best is None or d[0] < best:
            best = d[0]
            bestd = d
    print(bestd[1] * bestd[2])