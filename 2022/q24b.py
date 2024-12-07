import sys
import codelib as cl


def grid_graph(grid_dims, grid_neighbors, is_node):
    adj = dict()
    grids, gridr, gridh, gridw = grid_dims
    for s in range(grids):
        for t in range(gridr):
            for i in range(gridh+2):
                for j in range(gridw+2):
                    p = (s, t, i, j)
                    if not is_node(p):
                        continue
                    for q in grid_neighbors(p, is_node):
                        if not is_node(q):
                            continue
                        cl.dict_add_to_list(adj, p, q)
    return cl.dict_lambda_default(adj, [])


grid = []
for line in sys.stdin:
    ss = line.strip()
    if len(ss) > 0:
        grid.append(ss)

gridh, gridw = cl.grid_get_dims(grid)
gridh -= 2
gridw -= 2
gridr = gridh*gridw//cl.gcd(gridh, gridw)
grids = 3

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
    s, t, i, j = p
    return 0 <= s < grids and 0 <= t < gridr and 0 <= i < gridh+2 and 0 <= j < gridw+2 and grid[i][j] != '#' and (t, i, j) not in blizs


def is_goal(s, i, j):
    return (s, i, j) == (0, gridh+1, gridw) or (s, i, j) == (1, 0, 1)


def grid_neighbors(pos, is_node):
    neighbor_diffs = [(-1, 0), (0, -1), (0, 1), (1, 0), (0, 0)]
    s, t, i, j = pos
    for di, dj in neighbor_diffs:
        nexts = s+1 if is_goal(s, i+di, j+dj) else s
        pos_neighbor = (nexts, (t+1) % gridr, i+di, j+dj)
        if is_node(pos_neighbor):
            yield pos_neighbor


adj = grid_graph((grids, gridr, gridh, gridw), grid_neighbors, is_node=is_node)
dist = cl.shortest_path_bfs(adj, (0, 0, 0, 1))
ansf = min([dist[(grids-1, t, gridh+1, gridw)]
           for t in range(gridr) if (grids-1, t, gridh+1, gridw) in dist])
print(ansf)
