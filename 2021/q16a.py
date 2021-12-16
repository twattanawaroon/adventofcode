import sys
import codelib as cl


def parse(x, pos, step):
    return int(x[pos:pos+step], base=2), pos+step


def read_one(x, pos):
    ans = 0
    ver, pos = parse(x, pos, 3)
    ans += ver
    typ, pos = parse(x, pos, 3)
    if typ == 4:
        val = 0
        end = 1
        while end == 1:
            val <<= 4
            end, pos = parse(x, pos, 1)
            nmz, pos = parse(x, pos, 4)
            val += nmz
    else:
        lti, pos = parse(x, pos, 1)
        if lti == 0:
            leg, pos = parse(x, pos, 15)
            anz, pos = read_til(x, pos, pos+leg)
            ans += anz
        else:
            npk, pos = parse(x, pos, 11)
            for j in range(npk):
                anz, pos = read_one(x, pos)
                ans += anz
    return ans, pos


def read_til(x, pos, pen):
    ans = 0
    while pos < pen:
        anz, pos = read_one(x, pos)
        ans += anz
    return ans, pos


for line in sys.stdin:
    xt = line.strip()
    x = ''.join([f'{int(c, base=16):04b}' for c in xt])

ans, pos = read_one(x, 0)
print(ans)
