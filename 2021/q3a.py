import sys
x = []
xx = 0
yy = 0
for line in sys.stdin:
    x.append(line.strip())
f = []
for j in range(len(x[0])):
    f.append([])
for i in range(len(x)):
    for j in range(len(x[0])):
        f[j].append(x[i][j])
for j in range(len(x[0])):
    a0 = f[j].count('0')
    a1 = f[j].count('1')
    if a0 > a1:
        xx *= 2
        yy *= 2
        xx += 0
        yy += 1
    else:
        xx *= 2
        yy *= 2
        xx += 1
        yy += 0
print(xx*yy)