import sys

x = 0
y = 0
cdir = 0
dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

for line in sys.stdin:
    s = line.strip()
    c = s[0]
    d = int(s[1:])
    if c == 'E':
        x += d
    elif c == 'W':
        x -= d
    elif c == 'N':
        y += d
    elif c == 'S':
        y -= d
    elif c == 'R':
        cdir = (cdir+(d//90))%4
    elif c == 'L':
        cdir = (cdir+4-(d//90))%4
    else:
        dx, dy = dirs[cdir]
        x += dx*d
        y += dy*d
print(abs(x)+abs(y))