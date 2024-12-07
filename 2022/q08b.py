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
    tallest = None
    for j in range(m):
        z = 1
        score = 0
        for k in range(i-1, -1, -1):
            if x[k][j] < x[i][j]:
                score += 1
            else:
                score += 1
                break
        z *= score
        score = 0
        for k in range(i+1, n):
            if x[k][j] < x[i][j]:
                score += 1
            else:
                score += 1
                break
        z *= score
        score = 0
        for k in range(j-1, -1, -1):
            if x[i][k] < x[i][j]:
                score += 1
            else:
                score += 1
                break
        z *= score
        score = 0
        for k in range(j+1, m):
            if x[i][k] < x[i][j]:
                score += 1
            else:
                score += 1
                break
        z *= score
        y.append(z)

ansf = max(y)
print(ansf)
#submit(ansf, part="a", day=8, year=2022)