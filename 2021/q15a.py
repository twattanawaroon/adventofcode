import sys
import codelib as cl

x = []
for line in sys.stdin:
    x.append(list(map(int, line.strip())))

xdims = cl.grid_get_dims(x)
xh, xw = xdims
graph = cl.grid_wgraph4(xdims, lambda posa, posb: x[posb[0]][posb[1]])
gstart = (0, 0)
gend = (xh-1, xw-1)

print(cl.shortest_path_dijkstra(graph, gstart, gend))
