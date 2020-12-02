import sys
loop = (0, 1, 0, -1)

def matrix(a, b):
    return loop[((b+1)//(a+1))%4]

def run(x, offset, n):
    z = dict()
    p = dict()
    p[n] = 0
    for i in range(n-1, offset-1, -1):
        p[i] = p[i+1]+x[i]
    for i in range(offset, n):
        z[i] = abs(p[i])%10
    return z

for line in sys.stdin:
    r = line.strip()
    x = list(map(int, r))
    n = len(x)*10000
    offset = int(r[:7])
    y = dict()
    for i in range(offset, n):
        y[i] = x[i%len(x)]
    for t in range(100):
        y = run(y, offset, n)
    print(''.join(map(str,[y[i] for i in range(offset, offset+8)])))