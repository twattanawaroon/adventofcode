import sys
import codelib as cl

x = []
for line in sys.stdin:
    x.append(list(map(int, line.strip())))

xdims = cl.grid_get_dims(x)
xh, xw = xdims
count = 0

for coord in cl.grid_coords(x):
    if all([cl.grid_get(x, coord) < cl.grid_get(x, cn) for cn in cl.grid_neighbors4(xdims, coord)]):
        count += 1+cl.grid_get(x, coord)

print(count)
