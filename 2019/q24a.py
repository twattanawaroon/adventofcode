import sys
from collections import deque

def count(x, i, j):
    return 1 if (0 <= i < 5 and 0 <= j < 5 and x[i][j] == '#') else 0

def countAround(x, i, j):
    return count(x, i-1, j)+count(x, i+1, j)+count(x, i, j-1)+count(x, i, j+1)

def evolve(x):
    w = []
    for i in range(5):
        w.append(['.']*5)
    for i in range(5):
        for j in range(5):
            bugs = countAround(x, i, j)
            if (x[i][j] == '#' and bugs == 1) or (x[i][j] == '.' and 1 <= bugs <= 2):
                w[i][j] = '#'
            else:
                w[i][j] = '.'
    return w

def calcHash(x):
    ans = 0
    mul = 1
    for i in range(5):
        for j in range(5):
            ans += mul*count(x, i, j)
            mul *= 2
    return ans

x = []
s = set()
for line in sys.stdin:
    x.append([c for c in line.strip()])
s.add(calcHash(x))
while True:
    y = evolve(x)
    yc = calcHash(y)
    if yc in s:
        print(yc)
        break
    s.add(yc)
    x = y