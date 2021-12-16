import sys
import codelib as cl


def det(x, xh, xw, pos):
    pi, pj = pos
    gi, ri = divmod(pi, xh)
    gj, rj = divmod(pj, xw)
    return cl.mod_start1(cl.grid_get(x, (ri, rj)) + gi + gj, 9)


x = []
for line in sys.stdin:
    x.append(list(map(int, line.strip())))

xdims = cl.grid_get_dims(x)
xh, xw = xdims
graph = cl.grid_wgraph4(
    (5*xh, 5*xw), lambda posa, posb: det(x, xh, xw, posb))
gstart = (0, 0)
gend = (5*xh-1, 5*xw-1)

print(cl.shortest_path_dijkstra(graph, gstart, gend))
