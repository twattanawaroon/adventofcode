import sys
import codelib as cl
import collections

ds = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
coords = []
for line in sys.stdin:
    coords.append(tuple(map(int, line.strip().split(','))))

s = set(coords)
minx, maxx = cl.min_max(cl.coords_x(coords))
miny, maxy = cl.min_max(cl.coords_y(coords))
minz, maxz = cl.min_max(cl.coords_z(coords))

def flood(adj, start, s):
    ans = 0
    visited = set()
    visited.add(start)
    q = collections.deque()
    q.append(start)
    while len(q) > 0:
        p = q.popleft()
        for r in adj(p):
            if r in s:
                ans += 1
            elif r not in visited:
                visited.add(r)
                q.append(r)
    return ans

def adj6(pos):
    for d in ds:
        rx, ry, rz = cl.coord_offset(pos, d)
        if minx-1 <= rx <= maxx+1 and miny-1 <= ry <= maxy+1 and minz-1 <= rz <= maxz+1:
            yield (rx, ry, rz)

ansf = flood(adj6, (minx-1, miny-1, minz-1), s)
print(ansf)