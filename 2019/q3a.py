import sys

def get_line(line):
    segs = []
    y = list(line.strip().split(','))
    curx = 0
    cury = 0
    for item in y:
        ydir = item[0]
        ylen = int(item[1:])
        if ydir == 'R':
            (newx, newy) = (curx+ylen, cury)
        elif ydir == 'L':
            (newx, newy) = (curx-ylen, cury)
        elif ydir == 'U':
            (newx, newy) = (curx, cury+ylen)
        elif ydir == 'D':
            (newx, newy) = (curx, cury-ylen)
        segs.append((curx, cury, newx, newy))
        curx = newx
        cury = newy
    return segs

def dist(point):
    if point is None:
        return 10**100
    (pointx, pointy) = point
    return abs(pointx)+abs(pointy)

def get_orientation(seg):
    (x1,y1,x2,y2) = seg
    return x1 == x2

def get_intersect(seg1, seg2):
    if get_orientation(seg1) == get_orientation(seg2):
        return None
    if not get_orientation(seg1):
        seg0 = seg1
        seg1 = seg2
        seg2 = seg0
    (x1,y1,x2,y2) = seg1
    (x3,y3,x4,y4) = seg2
    if min(x3,x4) < x1 < max(x3,x4) and min(y1,y2) < y3 < max(y1,y2):
        return (x1,y3)
    return None

rays = []
for line in sys.stdin:
    rays.append(get_line(line))

best_point = None
for seg1 in rays[0]:
    for seg2 in rays[1]:
        point = get_intersect(seg1, seg2)
        if point is not None:
            if best_point is None or dist(point) < dist(best_point):
                best_point = point
print(dist(best_point))