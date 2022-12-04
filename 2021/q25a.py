import sys
import codelib as cl

x = []
for line in sys.stdin:
    x.append(line.strip())

def newloc(dims, px, py):
    dimh, dimw = dims
    return px%dimh, py%dimw

def move(xx):
    x = xx
    moved = False
    dims = cl.grid_get_dims(x)
    dimh, dimw = dims
    for round, rx, ry in [('>', 0, 1), ('v', 1, 0)]:
        y = []
        for i in range(dimh):
            y.append(['.'] * dimw)
        for i in range(dimh):
            for j in range(dimw):
                pi, pj = newloc(dims, i+rx, j+ry)
                if x[i][j] == round and x[pi][pj] == '.':
                    moved = True
                    y[pi][pj] = round
                elif x[i][j] != '.':
                    y[i][j] = x[i][j]
        x = y
    return y, moved

moved = True
st = 0
while moved:
    x, moved = move(x)
    st += 1

print(st)
