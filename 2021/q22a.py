import sys
import codelib as cl

cmds = []
for line in sys.stdin:
    c, v = line.strip().split()
    rs = []
    for dimm in v.split(','):
        d, rr = dimm.split('=')
        r1, r2 = rr.split('..')
        rs.append(int(r1))
        rs.append(int(r2))
    cmds.append((c, tuple(rs)))

ons = set()
for x in range(-50, 51):
    for y in range(-50, 51):
        for z in range(-50, 51):
            for cmd, rs in cmds:
                if rs[0] <= x <= rs[1] and rs[2] <= y <= rs[3] and rs[4] <= z <= rs[5]:
                    if cmd == 'on':
                        ons.add((x, y, z))
                    elif (x, y, z) in ons:
                        ons.remove((x, y, z))

print(len(ons))
