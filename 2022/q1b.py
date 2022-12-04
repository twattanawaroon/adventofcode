import sys
x = []
y = []
for line in sys.stdin:
    s = line.strip()
    if len(s) == 0:
        x.append(y[:])
        y.clear()
    else:
        y.append(int(line.strip()))
x.append(y[:])
s = sorted(list(map(sum, x)))[::-1]
print(sum(s[:3]))