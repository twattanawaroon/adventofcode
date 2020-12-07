import sys

global x, di, dj
size = 50
x = [line.strip() for line in sys.stdin]
di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0 ,1]

def obtain(pi, pj):
    global x, di, dj
    z = {'.': 0, '|': 0, '#': 0}
    for i in range(8):
        if 0 <= pi+di[i] < size and 0 <= pj+dj[i] < size:
            z[x[pi+di[i]][pj+dj[i]]] += 1
    return z

for t in range(10):
    y = ['']*size
    for i in range(size):
        for j in range(size):
            p = obtain(i, j)
            c = x[i][j]
            d = c
            if c == '.' and p['|'] >= 3:
                d = '|'
            elif c == '|' and p['#'] >= 3:
                d = '#'
            elif c == '#' and not (p['|'] >= 1 and p['#'] >= 1):
                d = '.'
            y[i] += d
    x = y

ans = {'.': 0, '|': 0, '#': 0}
for i in range(size):
    for j in range(size):
        ans[y[i][j]] += 1
print(ans['|']*ans['#'])