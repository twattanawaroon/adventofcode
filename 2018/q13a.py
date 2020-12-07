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

carts = []
locs = set()
a = [parse(line) for line in sys.stdin]
for y in range(len(a)):
    for x in range(len(a[y])):
        c = a[y][x]
        if c == '<':
            a[y][x] = '-'
            carts.append((y, x, '<', 0))
        elif c == '>':
            a[y][x] = '-'
            carts.append((y, x, '>', 0))
        elif c == '^':
            a[y][x] = '|'
            carts.append((y, x, '^', 0))
        elif c == 'v':
            a[y][x] = '|'
            carts.append((y, x, 'v', 0))

for cart in carts:
    y, x, d, m = cart
    locs.add((y, x))

ans = None
while True:
    carts.sort()
    print(carts)
    newcarts = []
    for cart in carts:
        y, x, d, m = cart
        ny, nx = move(y, x, d)
        nd = turn(d, a[ny][nx], m)
        nm = (m+1)%3 if a[ny][nx] == '+' else m
        if (ny, nx) in locs:
            ans = '%d,%d' % (nx, ny)
            break
        locs.remove((y, x))
        locs.add((ny, nx))
        newcarts.append((ny, nx, nd, nm))
    if ans is not None:
        break
    carts = newcarts
print(ans)