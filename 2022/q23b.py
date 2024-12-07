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

for rounds in range(10**20):
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
    moved = False
    for pos in newlocs:
        if newlocd[newlocs[pos]] == 1:
            es.remove(pos)
            es.add(newlocs[pos])
            moved = True
    if not moved:
        ansf = rounds+1
        break
    dirs.append(dirs.pop(0))

print(ansf)
