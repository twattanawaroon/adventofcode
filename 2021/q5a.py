import sys

def parse(item):
    g, h = item.split('->')
    g1, g2 = list(map(int,g.strip().split(',')))
    h1, h2 = list(map(int,h.strip().split(',')))
    return (g1,g2,h1,h2)

x = []
g = []
mx = 2000
for line in sys.stdin:
    x.append(parse(line.strip()))

for i in range(mx):
    g.append([0]*mx)

for line in x:
    x1, y1, x2, y2 = line
    if y1 == y2:
        for xx in range(min(x1,x2), max(x1,x2)+1):
            g[xx][y1] += 1
    elif x1 == x2:
        for yy in range(min(y1,y2), max(y1,y2)+1):
            g[x1][yy] += 1

ans = 0
for i in range(mx):
    for j in range(mx):
        if g[i][j] >= 2:
            ans += 1

print(ans)
