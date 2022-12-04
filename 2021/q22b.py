import sys
import codelib as cl


def positive(a):
    ax1, ax2, ay1, ay2, az1, az2 = a
    return ax1 < ax2 and ay1 < ay2 and az1 < az2


def subdiv(a, b):
    ax1, ax2, ay1, ay2, az1, az2 = a
    bx1, bx2, by1, by2, bz1, bz2 = b
    if ax2 <= bx1 or ax1 >= bx2 or ay2 <= by1 or ay1 >= by2 or az2 <= bz1 or az1 >= bz2:
        return [a]
    cx1 = max(ax1, bx1)
    cx2 = min(ax2, bx2)
    cy1 = max(ay1, by1)
    cy2 = min(ay2, by2)
    cs = [(ax1, bx1, ay1, ay2, az1, az2),
          (bx2, ax2, ay1, ay2, az1, az2),
          (cx1, cx2, ay1, by1, az1, az2),
          (cx1, cx2, by2, ay2, az1, az2),
          (cx1, cx2, cy1, cy2, az1, bz1),
          (cx1, cx2, cy1, cy2, bz2, az2)]
    return filter(positive, cs)


cmds = []
for line in sys.stdin:
    c, v = line.strip().split()
    rs = []
    for dimm in v.split(','):
        d, rr = dimm.split('=')
        r1, r2 = rr.split('..')
        rs.append(int(r1))
        rs.append(int(r2)+1)
    cmds.append((c, tuple(rs)))

blocks = []
for cmd, rs in cmds:
    nb = []
    for block in blocks:
        nb.extend(subdiv(block, rs))
    blocks = nb
    if cmd == 'on':
        blocks.append(rs)

print(sum([(x2-x1)*(y2-y1)*(z2-z1) for x1, x2, y1, y2, z1, z2 in blocks]))
