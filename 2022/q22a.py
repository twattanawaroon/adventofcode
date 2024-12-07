import sys
import codelib as cl
import re

turn_r = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}
turn_l = {(0, 1): (-1, 0), (1, 0): (0, 1), (0, -1): (1, 0), (-1, 0): (0, -1)}


def turn(face, dir):
    return turn_r[face] if dir == 'R' else turn_l[face]


grid = []
mode = False
for line in sys.stdin:
    s = line[:-1]
    if len(s) == 0:
        mode = True
    elif mode:
        cmds = s
    else:
        grid.append(s)

cmds = [c if c == 'L' or c == 'R' else int(
    c) for c in re.split(r'([LR])', cmds)]


def grid_get(grid, pos):
    try:
        return cl.grid_get(grid, pos)
    except:
        return ' '


gridh = len(grid)
gridw = max([len(row) for row in grid])
rmin = [min([c for c in range(gridw) if grid_get(grid, (r, c)) != ' '])
        for r in range(gridh)]
rmax = [max([c for c in range(gridw) if grid_get(grid, (r, c)) != ' '])
        for r in range(gridh)]
cmin = [min([r for r in range(gridh) if grid_get(grid, (r, c)) != ' '])
        for c in range(gridw)]
cmax = [max([r for r in range(gridh) if grid_get(grid, (r, c)) != ' '])
        for c in range(gridw)]


def valid_pos(pos):
    posr, posc = pos
    return 0 <= posr < gridh and rmin[posr] <= posc <= rmax[posr]


def potential_pos(pos, face):
    new_pos = cl.coord_offset(pos, face)
    if valid_pos(new_pos):
        return new_pos
    posr, posc = pos
    if face == (0, 1):
        return (posr, rmin[posr])
    elif face == (1, 0):
        return (cmin[posc], posc)
    elif face == (0, -1):
        return (posr, rmax[posr])
    elif face == (-1, 0):
        return (cmax[posc], posc)


def step(pos, face):
    new_pos = potential_pos(pos, face)
    if grid_get(grid, new_pos) == '#':
        return None
    return new_pos


pos = (0, rmin[0])
face = (0, 1)
for cmd in cmds:
    if cmd == 'L' or cmd == 'R':
        face = turn(face, cmd)
    else:
        for snum in range(cmd):
            new_pos = step(pos, face)
            if new_pos is None:
                break
            pos = new_pos

turn_a = {(0, 1): 0, (1, 0): 1, (0, -1): 2, (-1, 0): 3}
posr, posc = pos
ansf = (posr+1) * 1000 + (posc+1) * 4 + turn_a[face]
print(ansf)
