import sys
for line in sys.stdin:
    x = list(map(int, line.strip().split(',')))
    x[1] = 12
    x[2] = 2
    ptr = 0
    while x[ptr] != 99:
        if x[ptr] == 1:
            x[x[ptr+3]] = x[x[ptr+1]] + x[x[ptr+2]]
        elif x[ptr] == 2:
            x[x[ptr+3]] = x[x[ptr+1]] * x[x[ptr+2]]
        ptr += 4
    print(x[0])