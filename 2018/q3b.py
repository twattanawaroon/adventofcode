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
for rect1 in rects:
    idd1, x1, y1, w1, h1 = rect1
    fail = False
    for rect2 in rects:
        idd2, x2, y2, w2, h2 = rect2
        if idd1 != idd2 and not (x1+w1 <= x2 or x2+w2 <= x1 or y1+h1 <= y2 or y2+h2 <= y1):
            fail = True
            break
    if not fail:
        print(idd1)