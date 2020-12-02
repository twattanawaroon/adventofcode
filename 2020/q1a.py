import sys
x = []
for line in sys.stdin:
    x.append(int(line.strip()))
for i in range(len(x)):
    for j in range(i+1, len(x)):
        if x[i]+x[j] == 2020:
            print(x[i]*x[j])