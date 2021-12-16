import sys
import codelib as cl


def is_edge(c1, c2):
    return cl.grid_get(x, c1) < cl.grid_get(x, c2)


def is_node(c):
    return cl.grid_get(x, c) != 9


x = []
for line in sys.stdin:
    x.append(list(map(int, line.strip())))

xdims = cl.grid_get_dims(x)
xh, xw = xdims
graph = cl.grid_graph4(xdims, is_edge, is_node)
sizes = []
for coord in cl.grid_coords(x):
    if all([cl.grid_get(x, coord) < cl.grid_get(x, cn) for cn in cl.grid_neighbors4(xdims, coord)]):
        sizes.append(len(cl.reachable_bfs(graph, coord)))

sizes.sort()
print(cl.product(sizes[-3:]))
