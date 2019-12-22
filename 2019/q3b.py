import sys

def get_line(line):
    segs = []
    y = list(line.strip().split(','))
    curx = 0
    cury = 0
    tot = 0
    for item in y:
        ydir = item[0]
        ylen = int(item[1:])
        if ydir == 'R':
            (newx, newy) = (curx+ylen, cury)
            seg = ('H', curx, cury, ylen, 1, tot)
        elif ydir == 'L':
            (newx, newy) = (curx-ylen, cury)
            seg = ('H', curx-ylen, cury, ylen, -1, tot+ylen)
        elif ydir == 'U':
            (newx, newy) = (curx, cury+ylen)
            seg = ('V', curx, cury, ylen, 1, tot)
        elif ydir == 'D':
            (newx, newy) = (curx, cury-ylen)
            seg = ('V', curx, cury-ylen, ylen, -1, tot+ylen)
        segs.append(seg)
        curx = newx
        cury = newy
        tot += ylen
    return segs

def get_intersect_dist(seg1, seg2):
    if seg1[0] == seg2[0]:
        return None
    if seg1[0] == 'H':
        seg0 = seg1
        seg1 = seg2
        seg2 = seg0
    (d1,x1,y1,l1,z1,p1) = seg1
    (d3,x3,y3,l3,z3,p3) = seg2
    y2 = y1+l1
    x4 = x3+l3
    if min(x3,x4) < x1 < max(x3,x4) and min(y1,y2) < y3 < max(y1,y2):
        return p1+(y3-y1)*z1 + p3+(x1-x3)*z3
    return None

rays = []
for line in sys.stdin:
    rays.append(get_line(line))

best_point = None
for seg1 in rays[0]:
    for seg2 in rays[1]:
        d = get_intersect_dist(seg1, seg2)
        if d is not None:
            if best_point is None or d < best_point:
                best_point = d
print(best_point)