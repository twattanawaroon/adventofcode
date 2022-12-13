import sys
import codelib as cl
from aocd import submit

x = []
for line in sys.stdin:
    x.append([int(c) for c in line.strip()])

n = len(x)
m = len(x[0])
y = []
for i in range(n):
    y.append([False]*m)
for i in range(n):
    tallest = None
    for j in range(m):
        if tallest is None or x[i][j] > tallest:
            y[i][j] = True
            tallest = x[i][j]
for i in range(n):
    tallest = None
    for j in range(m-1,-1,-1):
        if tallest is None or x[i][j] > tallest:
            y[i][j] = True
            tallest = x[i][j]
for j in range(m):
    tallest = None
    for i in range(n):
        if tallest is None or x[i][j] > tallest:
            y[i][j] = True
            tallest = x[i][j]
for j in range(m):
    tallest = None
    for i in range(n-1,-1,-1):
        if tallest is None or x[i][j] > tallest:
            y[i][j] = True
            tallest = x[i][j]

ansf = 0
for i in range(n):
    for j in range(m):
        if y[i][j]:
            ansf += 1
print(ansf)
#submit(ansf, part="a", day=8, year=2022)