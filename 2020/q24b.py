import sys

d = {'e': (1, 0), 'ne': (1, 1), 'se': (0, -1),
     'w': (-1, 0), 'nw': (0, 1), 'sw': (-1, -1)}
p = set()

for line in sys.stdin:
    s = line.strip()
    x = 0
    y = 0
    i = 0
    while i < len(s):
        j = 1 if (s[i] == 'e' or s[i] == 'w') else 2
        dx, dy = d[s[i:i+j]]
        x += dx
        y += dy
        i += j
    if (x, y) in p:
        p.remove((x, y))
    else:
        p.add((x, y))

for tt in range(100):
    cands = set()
    np = set()
    for x, y in p:
        for dr in d:
            dx, dy = d[dr]
            cands.add((x+dx, y+dy))
    for x, y in cands:
        nb = 0
        for dr in d:
            dx, dy = d[dr]
            if (x+dx, y+dy) in p:
                nb += 1
        if (x, y) in p and 1 <= nb <= 2:
            np.add((x, y))
        elif (x, y) not in p and nb == 2:
            np.add((x, y))
    p = np

print(len(p))