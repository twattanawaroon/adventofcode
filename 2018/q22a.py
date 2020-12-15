import sys

for line in sys.stdin:
    p, q = line.split(':')
    if p.strip() == 'depth':
        depth = int(q)
    elif p.strip() == 'target':
        q1, q2 = q.strip().split(',')
        bx, by = int(q1), int(q2)

grid = []
for i in range(bx+1):
    grid.append([0]*(by+1))

for x in range(bx+1):
    for y in range(by+1):
        if x == 0 and y == 0:
            grid[x][y] = 0
        elif x == bx and y == by:
            grid[x][y] = 0
        elif y == 0:
            grid[x][y] = x*16807
        elif x == 0:
            grid[x][y] = y*48271
        else:
            grid[x][y] = grid[x-1][y]*grid[x][y-1]
        grid[x][y] = (grid[x][y]+depth)%20183

ans = 0
for x in range(bx+1):
    for y in range(by+1):
        ans += grid[x][y]%3

print(ans)