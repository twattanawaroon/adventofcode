import sys
sys.setrecursionlimit(10**7)

walls = []
xs = []
ys = []

for line in sys.stdin:
    p, q = line.split(',')
    ap, p0 = p.strip().split('=')
    aq, q0 = q.strip().split('=')
    q1, q2 = q0.split('..')
    walls.append((ap, int(p0), aq, int(q1), int(q2)))
    if ap == 'x':
        xs.append(int(p0))
        ys.append(int(q1))
        ys.append(int(q2))
    else:
        ys.append(int(p0))
        xs.append(int(q1))
        xs.append(int(q2))

minx = min(xs)-1
maxx = max(xs)+1
miny = min(ys)
maxy = max(ys)
grid = []

for i in range(maxy-miny+1):
    grid.append(['.']*(maxx-minx+1))

for p, p0, q, q1, q2 in walls:
    if p == 'x':
        for i in range(q1, q2+1):
            grid[i-miny][p0-minx] = '#'
    else:
        for i in range(q1, q2+1):
            grid[p0-miny][i-minx] = '#'

def drop(gy, gx):
    grid[gy][gx] = '|'
    return gy+1 <= maxy-miny and fountain(gy+1, gx)

def fountain(gy, gx):
    if grid[gy][gx] == '#' or grid[gy][gx] == '~':
        return True
    grid[gy][gx] = '|'
    spreadLeft = False
    spreadRight = False
    if gy+1 <= maxy-miny and fountain(gy+1, gx):
        for hx in range(gx-1, -1, -1):
            if grid[gy][hx] == '#':
                spreadLeft = True
                break
            elif not (grid[gy][hx] == '.' and drop(gy, hx)):
                break
        for hx in range(gx+1, maxx-minx+1):
            if grid[gy][hx] == '#':
                spreadRight = True
                break
            elif not (grid[gy][hx] == '.' and drop(gy, hx)):
                break
        if not (spreadLeft and spreadRight):
            return False
        grid[gy][gx] = '~'
        for hx in range(gx-1, -1, -1):
            if grid[gy][hx] == '#':
                break
            else:
                grid[gy][hx] = '~'
        for hx in range(gx+1, maxx-minx+1):
            if grid[gy][hx] == '#':
                break
            else:
                grid[gy][hx] = '~'
        return True
    return False

fountain(0, 500-minx)
print(sum([row.count('~') for row in grid]))
