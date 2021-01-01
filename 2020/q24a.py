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
print(len(p))
