import sys

mask = None
m = dict()

def digit(mask, val):
    if mask == 'X':
        return val
    else:
        return int(mask)

def masked(mask, val):
    x = []
    for i in range(len(mask)):
        x.append(val%2)
        val //= 2
    x = x[::-1]
    ans = 0
    for i in range(len(mask)):
        ans *= 2
        ans += digit(mask[i], x[i])
    return(ans)

for line in sys.stdin:
    s, traw = line.strip().split('=')
    if s.strip() == 'mask':
        mask = traw.strip()
    else:
        addr = int(s.strip()[4:-1])
        m[addr] = masked(mask, int(traw.strip()))

print(sum([m[x] for x in m]))