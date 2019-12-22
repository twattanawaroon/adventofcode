import sys

def test(x, a, b):
    x[1] = a
    x[2] = b
    ptr = 0
    while x[ptr] != 99:
        if x[ptr] == 1:
            x[x[ptr+3]] = x[x[ptr+1]] + x[x[ptr+2]]
        elif x[ptr] == 2:
            x[x[ptr+3]] = x[x[ptr+1]] * x[x[ptr+2]]
        else:
            return False
        ptr += 4
    return x[0] == 19690720

for line in sys.stdin:
    y = list(map(int, line.strip().split(',')))
    for a in range(100):
        for b in range(100):
            if test(y[:], a, b):
                print(a*100+b)