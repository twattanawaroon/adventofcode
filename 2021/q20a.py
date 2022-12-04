import sys
import codelib as cl

MM = 4
MQ = 3

def get(img, dims, i, j, assume):
    if cl.grid_inside(dims, (i, j)):
        return img[i][j]
    else:
        return assume

def calc(enc, img, dims, i ,j, assume):
    v = 0
    for di in range(-MQ, -MQ+3):
        for dj in range(-MQ, -MQ+3):
            v *= 2
            v += 1 if get(img, dims, i+di, j+dj, assume) == '#' else 0
    return enc[v]

enc = None
img = []
for line in sys.stdin:
    s = line.strip()
    if enc is None:
        enc = s
    elif len(s) > 0:
        img.append(s)
print(enc)

for round in range(50):
    h = len(img)
    w = len(img[0])
    newimg = []
    for i in range(h+MM):
        a = '.' if (round%2) == 0 else '#'
        newimg.append([calc(enc, img, (h, w), i, j, a) for j in range(w+MM)])
    img = newimg



ans = 0
h = len(img)
w = len(img[0])

for i in range(h):
    print(''.join(img[i]))

for i in range(h):
    for j in range(w):
        if img[i][j] == '#':
            ans += 1
print(ans)
