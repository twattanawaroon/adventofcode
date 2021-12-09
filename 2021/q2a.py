import sys
x = []
xx = 0
yy = 0
for line in sys.stdin:
    x.append(line.strip().split())
for i in range(len(x)):
    d, m = x[i]
    if d[0] == 'f':
        xx += int(m)
    elif d[0] == 'd':
        yy += int(m)
    else:
        yy -= int(m)
print(xx*yy)