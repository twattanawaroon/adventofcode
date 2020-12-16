import sys

mask = None
m = dict()

def rec(m, mask, x, i, addr, val):
    if i >= len(mask):
        m[addr] = val
    elif mask[i] == '0':
        rec(m, mask, x, i+1, addr*2+x[i], val)
    elif mask[i] == '1':
        rec(m, mask, x, i+1, addr*2+1, val)
    else:
        rec(m, mask, x, i+1, addr*2+0, val)
        rec(m, mask, x, i+1, addr*2+1, val)

def assign(m, mask, addr, val):
    x = []
    for i in range(len(mask)):
        x.append(addr%2)
        addr //= 2
    x = x[::-1]
    rec(m, mask, x, 0, 0, val)

for line in sys.stdin:
    s, traw = line.strip().split('=')
    if s.strip() == 'mask':
        mask = traw.strip()
    else:
        addr = int(s.strip()[4:-1])
        assign(m, mask, addr, int(traw.strip()))

print(sum([m[x] for x in m]))