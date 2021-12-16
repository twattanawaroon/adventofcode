import sys

score = 0
x = []
for line in sys.stdin:
    x.append(list(map(int,line.strip())))

for step in range(100):
    for i in range(len(x)):
        for j in range(len(x[0])):
            x[i][j] += 1
    fl = True
    s = set()
    while fl:
        fl = False
        for i in range(len(x)):
            for j in range(len(x[0])):
                if x[i][j] > 9 and (i, j) not in s:
                    s.add((i, j))
                    score += 1
                    fl = True
                    for ii in [-1, 0, 1]:
                        for jj in [-1, 0, 1]:
                            if 0 <= i+ii < len(x) and 0 <= j+jj < len(x[0]):
                                x[i+ii][j+jj] += 1
    for i in range(len(x)):
        for j in range(len(x[0])):
            if x[i][j] > 9:
                x[i][j] = 0
print(score)
