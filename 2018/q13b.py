import sys

def parse(strin):
    return [c for c in strin]

def move(zy, zx, zd):
    mmap = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
    dy, dx = mmap[zd]
    return zy+dy, zx+dx

def turn(zd, zt, zm):
    if zt == '\\':
        mmap = {'<': '^', '>': 'v', '^': '<', 'v': '>'}
        return mmap[zd]
    elif zt == '/':
        mmap = {'<': 'v', '>': '^', '^': '>', 'v': '<'}
        return mmap[zd]
    elif zt == '+':
        mmap0 = {'<': 'v', '>': '^', '^': '<', 'v': '>'}
        mmap1 = {'<': '<', '>': '>', '^': '^', 'v': 'v'}
        mmap2 = {'<': '^', '>': 'v', '^': '>', 'v': '<'}
        mmap = [mmap0, mmap1, mmap2]
        return mmap[zm][zd]
    else:
        return zd

allcarts = []
locs = {}
a = [parse(line) for line in sys.stdin]
cnum = 0
for y in range(len(a)):
    for x in range(len(a[y])):
        c = a[y][x]
        if c == '<':
            a[y][x] = '-'
            allcarts.append((y, x, '<', 0))
        elif c == '>':
            a[y][x] = '-'
            allcarts.append((y, x, '>', 0))
        elif c == '^':
            a[y][x] = '|'
            allcarts.append((y, x, '^', 0))
        elif c == 'v':
            a[y][x] = '|'
            allcarts.append((y, x, 'v', 0))

alive = [True]*len(allcarts)

for i in range(len(allcarts)):
    y, x, d, m = allcarts[i]
    locs[(y, x)] = i

while sum(alive) > 1:
    carts = []
    for i in range(len(allcarts)):
        if alive[i]:
            y, x, d, m = allcarts[i]
            carts.append((y, x, d, m, i))
    carts.sort()
    for cart in carts:
        y, x, d, m, c = cart
        if not alive[c]:
            continue
        ny, nx = move(y, x, d)
        nd = turn(d, a[ny][nx], m)
        nm = (m+1)%3 if a[ny][nx] == '+' else m
        del locs[(y, x)]
        if (ny, nx) in locs:
            alive[c] = False
            alive[locs[(ny, nx)]] = False
            del locs[(ny, nx)]
        else:
            locs[(ny, nx)] = c
        allcarts[c] = (ny, nx, nd, nm)

for i in range(len(allcarts)):
    if alive[i]:
        y, x, d, m = allcarts[i]
        ans = '%d,%d' % (x, y)
        break

print(ans)