import sys

def triangle(c):
    return (c*(c+1))//2

for line in sys.stdin:
    x = list(map(int,line.strip().split(',')))
    x.sort()
    ans = None
    for med in range(x[0], x[-1]+1):
        v = sum([triangle(abs(med-c)) for c in x])
        if ans is None or v < ans:
            ans = v
    print(ans)
