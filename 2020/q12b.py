import sys

x = 0
y = 0
wx = 10
wy = 1

def rot(px, py, tt):
    for ii in range(tt):
        px, py = py, -px
    return px, py

for line in sys.stdin:
    s = line.strip()
    c = s[0]
    d = int(s[1:])
    if c == 'E':
        wx += d
    elif c == 'W':
        wx -= d
    elif c == 'N':
        wy += d
    elif c == 'S':
        wy -= d
    elif c == 'R':
        wx, wy = rot(wx, wy, d//90)
    elif c == 'L':
        wx, wy = rot(wx, wy, 4-(d//90))
    else:
        x += wx*d
        y += wy*d
print(abs(x)+abs(y))