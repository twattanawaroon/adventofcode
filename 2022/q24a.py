import sys
import codelib as cl


def grid_graph(grid_dims, grid_neighbors, is_node):
    adj = dict()
    gridr, gridh, gridw = grid_dims
    for t in range(gridr):
        for i in range(gridh+2):
            for j in range(gridw+2):
                p = (t, i, j)
                if not is_node(p):
                    continue
                for q in grid_neighbors(p, is_node):
                    if not is_node(q):
                        continue
                    cl.dict_add_to_list(adj, p, q)
    return cl.dict_lambda_default(adj, [])


grid = []
for line in sys.stdin:
    s = line.strip()
    if len(s) > 0:
        grid.append(s)

gridh, gridw = cl.grid_get_dims(grid)
gridh -= 2
gridw -= 2
gridr = gridh*gridw//cl.gcd(gridh, gridw)

blizs = set()
for i in range(gridh):
    for j in range(gridw):
        c = grid[i+1][j+1]
        if c == '>':
            move = (0, 1)
        elif c == '<':
            move = (0, -1)
        elif c == '^':
            move = (-1, 0)
        elif c == 'v':
            move = (1, 0)
        else:
            continue
        for t in range(gridr):
            movei, movej = move
            newi = (i+t*movei) % gridh
            newj = (j+t*movej) % gridw
            blizs.add((t, newi+1, newj+1))


def is_node(p):
    t, i, j = p
    return 0 <= t < gridr and 0 <= i < gridh+2 and 0 <= j < gridw+2 and grid[i][j] != '#' and (t, i, j) not in blizs


def grid_neighbors(pos, is_node):
    neighbor_diffs = [(-1, 0), (0, -1), (0, 1), (1, 0), (0, 0)]
    t, i, j = pos
    for di, dj in neighbor_diffs:
        pos_neighbor = ((t+1) % gridr, i+di, j+dj)
        if is_node(pos_neighbor):
            yield pos_neighbor


adj = grid_graph((gridr, gridh, gridw), grid_neighbors, is_node=is_node)
dist = cl.shortest_path_bfs(adj, (0, 0, 1))
ansf = min([dist[(t, gridh+1, gridw)]
           for t in range(gridr) if (t, gridh+1, gridw) in dist])
print(ansf)
