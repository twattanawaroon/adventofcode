import sys

def process(text):
    return int(text.strip())

def c(x, y, ser):
    p = ((x+10)*y+ser)*(x+10)
    return ((p//100)%10)-5

def square(x, x1, y1, x2, y2):
    return x[x1][y1]+x[x2][y2]-x[x1][y2]-x[x2][y1]

inp = [process(line) for line in sys.stdin]
for ser in inp:
    best = None
    bestc = None
    x = []
    for i in range(301):
        x.append([0]*301)
    for i in range(1, 301):
        for j in range(1, 301):
            x[i][j] = c(i, j, ser)
            x[i][j] += x[i-1][j]+x[i][j-1]-x[i-1][j-1]
    for i in range(1, 301):
        for j in range(1, 301):
            for k in range(301-max(i,j)):
                score = square(x, i-1, j-1, i+k, j+k)
                if best is None or score > best:
                    best = score
                    bestc = (i, j, k+1)
    print(bestc)