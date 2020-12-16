import sys

x = []
for line in sys.stdin:
    x.append(int(line.strip()))

m = [0]*4
x.sort()
for i in range(1, len(x)):
    m[x[i]-x[i-1]] += 1
m[x[0]] += 1
m[3] += 1

print(m[1]*m[3])