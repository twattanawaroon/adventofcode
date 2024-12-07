import sys
import codelib as cl

for line in sys.stdin:
    seq = line.strip()

pieces = [[(0, 0), (0, 1), (0, 2), (0, 3)],
          [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
          [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],
          [(0, 0), (1, 0), (2, 0), (3, 0)],
          [(0, 0), (0, 1), (1, 0), (1, 1)], ]

si = 0
pi = 0
maxh = 0
grid = set()


def shift(piece, d):
    return [cl.coord_offset(p, d) for p in piece]


def ok_cell(c, grid):
    cx, cy = c
    return 0 <= cy < 7 and 1 <= cx and (cx, cy) not in grid


def ok(piece, grid):
    return all(map(lambda c: ok_cell(c, grid), piece))


for pc in range(2022):
    piece = shift(pieces[pi], (maxh+4, 2))
    down = True
    while down:
        sc = seq[si]
        si += 1
        si %= len(seq)
        new_piece = shift(piece, (0, -1 if sc == '<' else 1))
        if ok(new_piece, grid):
            piece = new_piece
        new_piece = shift(piece, (-1, 0))
        if ok(new_piece, grid):
            piece = new_piece
        else:
            down = False
    grid |= set(piece)
    maxh = max(maxh, max(cl.coords_x(piece)))
    pi += 1
    pi %= 5

print(maxh)
