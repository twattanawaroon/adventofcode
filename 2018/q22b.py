import sys
import heapq
from collections import deque

for line in sys.stdin:
    p, q = line.split(':')
    if p.strip() == 'depth':
        depth = int(q)
    elif p.strip() == 'target':
        q1, q2 = q.strip().split(',')
        bx, by = int(q1), int(q2)

grid = []
mx = max(1000, bx*2)
my = max(1000, by*2)
for i in range(mx):
    grid.append([0]*(my))

for x in range(mx):
    for y in range(my):
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

def move(grid, dist, q, px, py, pt, pd):
    if not (0 <= px < mx and 0 <= py < my):
        return
    if grid[px][py]%3 == pt:
        return
    if (px, py, pt) in dist and dist[(px, py, pt)] <= pd:
        return
    dist[(px, py, pt)] = pd
    heapq.heappush(q, (pd, (px, py, pt)))

def sssp(grid, s, t):
    q = [(0, s)]
    dist = dict()
    dist[s] = 0
    visited = set()
    while len(q) > 0:
        pd, pnode = heapq.heappop(q)
        if pnode in visited:
            continue
        visited.add(pnode)
        if pnode == t:
            return dist[pnode]
        px, py, pt = pnode
        move(grid, dist, q, px-1, py, pt, pd+1)
        move(grid, dist, q, px+1, py, pt, pd+1)
        move(grid, dist, q, px, py-1, pt, pd+1)
        move(grid, dist, q, px, py+1, pt, pd+1)
        move(grid, dist, q, px, py, (pt+1)%3, pd+7)
        move(grid, dist, q, px, py, (pt+2)%3, pd+7)
    return None

print(sssp(grid, (0, 0, 1), (bx, by, 1)))