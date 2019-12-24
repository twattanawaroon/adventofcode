import sys
from collections import deque

LL = 200

def count(x, l, i, j):
    return 1 if (0 <= l <= 2*LL and 0 <= i < 5 and 0 <= j < 5 and x[l][i][j] == '#') else 0

def countAround(x, l, i, j):
    cnt = 0
    # up
    if i == 0:
        cnt += count(x, l-1, 1, 2)
    elif i == 3 and j == 2:
        cnt += sum([count(x, l+1, 4, k) for k in range(5)])
    else:
        cnt += count(x, l, i-1, j)
    # down
    if i == 4:
        cnt += count(x, l-1, 3, 2)
    elif i == 1 and j == 2:
        cnt += sum([count(x, l+1, 0, k) for k in range(5)])
    else:
        cnt += count(x, l, i+1, j)
    # left
    if j == 0:
        cnt += count(x, l-1, 2, 1)
    elif i == 2 and j == 3:
        cnt += sum([count(x, l+1, k, 4) for k in range(5)])
    else:
        cnt += count(x, l, i, j-1)
    # right
    if j == 4:
        cnt += count(x, l-1, 2, 3)
    elif i == 2 and j == 1:
        cnt += sum([count(x, l+1, k, 0) for k in range(5)])
    else:
        cnt += count(x, l, i, j+1)
    # answer
    return cnt

def evolve(x):
    w = []
    for l in range(2*LL+1):
        wl = []
        for i in range(5):
            wl.append(['.']*5)
        w.append(wl)
    for l in range(2*LL+1):
        for i in range(5):
            for j in range(5):
                if i == 2 and j == 2:
                    continue
                bugs = countAround(x, l, i, j)
                if (x[l][i][j] == '#' and bugs == 1) or (x[l][i][j] == '.' and 1 <= bugs <= 2):
                    w[l][i][j] = '#'
                else:
                    w[l][i][j] = '.'
    return w

x = []
for l in range(2*LL+1):
    xl = []
    for i in range(5):
        xl.append(['.']*5)
    x.append(xl)
xl = []
for line in sys.stdin:
    xl.append([c for c in line.strip()])
x[LL] = xl
for t in range(LL):
    y = evolve(x)
    x = y
ans = 0
for l in range(2*LL+1):
    for i in range(5):
        for j in range(5):
            ans += count(x, l, i, j)
print(ans)