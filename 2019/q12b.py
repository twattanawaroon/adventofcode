import sys
from functools import reduce

def parse(s):
    ans = []
    l = s[1:-1].split(',')
    for item in l:
        ans.append(int(item.split('=')[1]))
    return ans

p = []
v = []
nn = []
aa = []

def gcd(vp, vq):
    if vp < vq:
        wp, wq = vq, vp
    else:
        wp, wq = vp, vq
    while wq > 0:
        wr = wp % wq
        wp = wq
        wq = wr
    return wp

def lcm(vp, vq):
    return vp*vq//gcd(vp,vq)

for line in sys.stdin:
    b = line.strip()
    p.append(parse(b))
    v.append([0,0,0])

for dim in range(3):
    hist = dict()
    timestep = 0
    while True:
        for i in range(len(p)):
            for j in range(len(p)):
                if i == j:
                    continue
                if p[i][dim] < p[j][dim]:
                    v[i][dim] += 1
                elif p[i][dim] > p[j][dim]:
                    v[i][dim] -= 1
        pol = []
        for i in range(len(p)):
            p[i][dim] += v[i][dim]
            pol.append(p[i][dim])
            pol.append(v[i][dim])
        pos = tuple(pol)
        if pos in hist:
            break
        hist[pos] = timestep
        timestep += 1
    nval = timestep-hist[pos]
    aval = timestep%nval
    nn.append(nval)
    aa.append(aval)

l = list(zip(nn,aa))
x = reduce(lambda a,b: a*b[0], l, 1)
ans = sum(x//a*b*pow(x//a, a-2, a) for a,b in l)
while ans <= 0:
    ans = reduce(lambda a,b: lcm(a,b), nn)
print(ans)