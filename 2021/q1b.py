import sys
x = []
count = 0
for line in sys.stdin:
    x.append(int(line.strip()))
for i in range(3,len(x)):
    if x[i] > x[i-3]:
        count += 1
print(count)