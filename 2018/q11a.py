import sys

def process(text):
    return int(text.strip())

def c(x, y, ser):
    p = ((x+10)*y+ser)*(x+10)
    return ((p//100)%10)-5

inp = [process(line) for line in sys.stdin]
for ser in inp:
    best = None
    bestc = None
    for i in range(1, 299):
        for j in range(1, 299):
            score = sum([c(i+di, j+dj, ser) for di in range(3) for dj in range(3)])
            if best is None or score > best:
                best = score
                bestc = (i, j)
    print(bestc)