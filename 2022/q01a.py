import sys
import codelib as cl

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
print(max(map(sum, x)))
