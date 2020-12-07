import sys

global s, si, ans
z = [line.strip() for line in sys.stdin]
s = z[0].split()
si = 0
ans = 0

def read():
    global s, si, ans
    c = s[si]
    si += 1
    return int(c)

def node():
    global ans
    children = read()
    mets = read()
    for i in range(children):
        node()
    for i in range(mets):
        x = read()
        ans += x

node()
print(ans)