import sys
import codelib as cl

ds = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
coords = []
for line in sys.stdin:
    coords.append(tuple(map(int, line.strip().split(','))))

ansf = 6*len(coords)
s = set(coords)
for pos in coords:
    for d in ds:
        if cl.coord_offset(pos, d) in s:
            ansf -= 1
print(ansf)