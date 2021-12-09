import sys

x = []
f = [0]*9
for line in sys.stdin:
    x.extend(list(map(int,line.strip().split(','))))

for item in x:
    f[item] += 1

for day in range(80):
    n = f[0]
    for i in range(8):
        f[i] = f[i+1]
    f[6] += n
    f[8] = n

print(sum(f))
