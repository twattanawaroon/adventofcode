import sys

s = set()
newset = True
ans = 0
for line in sys.stdin:
    x = line.strip()
    if len(x) == 0:
        ans += len(s)
        s.clear()
        newset = True
    else:
        t = set(x)
        if newset:
            s = t
            newset = False
        else:
            s &= t
ans += len(s)

print(ans)
