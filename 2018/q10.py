import sys

def parse(ins):
    ins_left = ins.strip().split('<')
    posr, tmp1 = ins_left[1].split('>')
    velr, tmp2 = ins_left[2].split('>')
    posx, posy = map(int, posr.split(','))
    velx, vely = map(int, velr.split(','))
    return posx, posy, velx, vely

x = [parse(line) for line in sys.stdin]
bestbox = None
besti = -1
for i in range(10036, 10037):
    xs = []
    ys = []
    for posx, posy, velx, vely in x:
        lx = posx + velx*i
        ly = posy + vely*i
        xs.append(lx)
        ys.append(ly)
    box = (max(xs)-min(xs))*(max(ys)-min(ys))
    if bestbox is None or bestbox > box:
        bestbox = box
        besti = i
    grid = []
    for j in range(max(ys)-min(ys)+1):
        grid.append(['.'] * (max(xs)-min(xs)+1))
    for j in range(len(xs)):
        lx = xs[j]-min(xs)
        ly = ys[j]-min(ys)
        grid[ly][lx] = '#'
    print(i)
    for i in range(max(ys)-min(ys)+1):
        print(''.join(grid[i]))
print(bestbox, besti)