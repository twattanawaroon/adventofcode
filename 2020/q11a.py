import sys

x = []
for line in sys.stdin:
    x.append([c for c in line.strip()])

diffs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def occ(x, pi, pj):
    if not (0 <= pi < len(x) and 0 <= pj < len(x[0])):
        return False
    return x[pi][pj] == '#'

stab = False
while not stab:
    stab = True
    y = []
    for line in x:
        y.append(line[:])
    for i in range(len(x)):
        for j in range(len(x[0])):
            if x[i][j] == 'L' and sum([occ(x, i+di, j+dj) for di, dj in diffs]) == 0:
                y[i][j] = '#'
                stab = False
            elif x[i][j] == '#' and sum([occ(x, i+di, j+dj) for di, dj in diffs]) >= 4:
                y[i][j] = 'L'
                stab = False
    x = y

print(sum([s.count('#') for s in x]))