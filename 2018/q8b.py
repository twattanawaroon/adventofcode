import sys

global s, si, ans
z = [line.strip() for line in sys.stdin]
s = z[0].split()
si = 0

def read():
    global s, si, ans
    c = s[si]
    si += 1
    return int(c)

def node():
    global ans
    children = read()
    mets = read()
    v = [node() for i in range(children)]
    t = [read() for i in range(mets)]
    if children == 0:
        return sum(t)
    else:
        return sum([v[u-1] if 1 <= u <= children else 0 for u in t])

print(node())