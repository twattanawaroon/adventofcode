import sys
x = []
for line in sys.stdin:
    x.append(int(line.strip()))
s = set(x)
for i in range(len(x)):
    for j in range(i+1, len(x)):
        k = 2020-x[i]-x[j]
        if k in s:
            print(x[i]*x[j]*k)