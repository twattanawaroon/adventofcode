import sys
MX = 1024

def process(text):
    idraw, restraw = text.strip().split('@')
    idd = int(idraw.strip()[1:])
    posraw, dimraw = restraw.strip().split(':')
    x, y = map(int, posraw.strip().split(','))
    w, h = map(int, dimraw.strip().split('x'))
    return (idd, x, y, w, h)

grid = []
for i in range(MX):
    grid.append([0] * MX)

rects = [process(line) for line in sys.stdin]
for rect in rects:
    idd, x, y, w, h = rect
    for i in range(x, x+w):
        for j in range(y, y+h):
            grid[i][j] += 1

ans = 0
for i in range(MX):
    for j in range(MX):
        if grid[i][j] >= 2:
            ans += 1
print(ans)