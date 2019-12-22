import sys
loop = (0, 1, 0, -1)

def matrix(a, b):
    return loop[((b+1)//(a+1))%4]

def run(x):
    return [abs(sum([x[j]*matrix(i,j) for j in range(len(x))])) % 10 for i in range(len(x))]

for line in sys.stdin:
    x = list(map(int, line.strip()))
    for t in range(100):
        x = run(x)
    print(''.join(map(str,x[:8])))