import sys
OFFSET = 300
MX = 1000

def process(text):
    x, y = map(int, text.strip().split(','))
    return (x+OFFSET, y+OFFSET)

points = [process(line) for line in sys.stdin]
area = [0] * len(points)
iinf = [False] * len(points)
for i in range(MX):
    for j in range(MX):
        closest = None
        closeit = None
        for k in range(len(points)):
            x, y = points[k]
            dist = abs(x-i)+abs(y-j)
            if closest is None or dist < closest:
                closest = dist
                closeit = k
            elif dist == closest:
                closeit = None
        if closeit is not None:
            if i == 0 or i == MX-1 or j == 0 or j == MX-1:
                iinf[closeit] = True
            else:
                area[closeit] += 1
print(max([0 if y else x for (x, y) in zip(area, iinf)]))
