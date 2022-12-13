import sys
import codelib as cl

grid = []
for line in sys.stdin:
    grid.append([c for c in line.strip()])

def check(p, q):
    return ord(cl.grid_get(grid, p)) - ord(cl.grid_get(grid, q)) >= -1

dims = cl.grid_get_dims(grid)
for pos in cl.grid_coords(grid):
    if cl.grid_get(grid, pos) == 'S':
        ps = pos
        cl.grid_set(grid, pos, 'a')
    elif cl.grid_get(grid, pos) == 'E':
        pe = pos
        cl.grid_set(grid, pos, 'z')
adj = cl.grid_graph4(dims, is_edge=check)
dist = cl.shortest_path_bfs(adj, ps)
ansf = dist[pe]

print(ansf)
