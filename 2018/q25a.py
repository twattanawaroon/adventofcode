import sys

x = []
visited = set()
for line in sys.stdin:
    x.append(tuple(map(int, line.strip().split(','))))

def dist(i, j):
    return sum([abs(x[i][k]-x[j][k]) for k in range(4)])

def dfs(p):
    visited.add(p)
    for i in range(len(x)):
        if i not in visited and dist(p, i) <= 3:
            dfs(i)

count = 0
for i in range(len(x)):
    if i not in visited:
        dfs(i)
        count += 1
print(count)