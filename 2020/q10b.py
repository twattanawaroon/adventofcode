import sys

x = [0]
for line in sys.stdin:
    x.append(int(line.strip()))

x.sort()
m = [0]*len(x)
m[0] = 1

for i in range(1, len(x)):
    for j in range(4):
        if i-j >= 0 and x[i]-x[i-j] <= 3:
            m[i] += m[i-j]

print(m[-1])