import sys
import codelib as cl

g = []
dirs = [
    ((-1, 0), [(-1, -1), (-1, 0), (-1, 1)]),
    ((1, 0), [(1, -1), (1, 0), (1, 1)]),
    ((0, -1), [(-1, -1), (0, -1), (1, -1)]),
    ((0, 1), [(-1, 1), (0, 1), (1, 1)]),
]
all8 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

ansf = 0
for line in sys.stdin:
    g.append(line.strip())

es = set()
for i in range(len(g)):
    gs = g[i]
    for j in range(len(gs)):
        if gs[j] == '#':
            es.add((i, j))

for rounds in range(10):
    newlocs = dict()
    newlocd = dict()
    for pos in es:
        if all([cl.coord_offset(pos, check) not in es for check in all8]):
            continue
        for dir, checks in dirs:
            if all([cl.coord_offset(pos, check) not in es for check in checks]):
                newlocs[pos] = cl.coord_offset(pos, dir)
                cl.dict_inc(newlocd, cl.coord_offset(pos, dir))
                break
    for pos in newlocs:
        if newlocd[newlocs[pos]] == 1:
            es.remove(pos)
            es.add(newlocs[pos])
    dirs.append(dirs.pop(0))

minx, maxx = cl.min_max(cl.coords_x(es))
miny, maxy = cl.min_max(cl.coords_y(es))
ansf = (maxx-minx+1)*(maxy-miny+1)-len(es)
print(ansf)
