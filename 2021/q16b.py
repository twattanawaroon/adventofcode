import sys
import codelib as cl


def parse(x, pos, step):
    return int(x[pos:pos+step], base=2), pos+step


def read_one(x, pos):
    ans = []
    ver, pos = parse(x, pos, 3)
    typ, pos = parse(x, pos, 3)
    if typ == 4:
        val = 0
        end = 1
        while end == 1:
            val <<= 4
            end, pos = parse(x, pos, 1)
            nmz, pos = parse(x, pos, 4)
            val += nmz
        return val, pos
    else:
        lti, pos = parse(x, pos, 1)
        if lti == 0:
            leg, pos = parse(x, pos, 15)
            ans, pos = read_til(x, pos, pos+leg)
        else:
            npk, pos = parse(x, pos, 11)
            for j in range(npk):
                anz, pos = read_one(x, pos)
                ans.append(anz)
        reducers = [sum, cl.product, min, max, None,
                    lambda z: 1 if (z[0] > z[1]) else 0,
                    lambda z: 1 if (z[0] < z[1]) else 0,
                    lambda z: 1 if (z[0] == z[1]) else 0]
        return reducers[typ](ans), pos


def read_til(x, pos, pen):
    ans = []
    while pos < pen:
        anz, pos = read_one(x, pos)
        ans.append(anz)
    return ans, pos


for line in sys.stdin:
    xt = line.strip()
    x = ''.join([f'{int(c, base=16):04b}' for c in xt])

ans, pos = read_one(x, 0)
print(ans)
