import sys

s = set()
ans = 0
for line in sys.stdin:
    x = line.strip()
    if len(x) == 0:
        ans += len(s)
        s.clear()
    else:
        for c in x:
            s.add(c)
ans += len(s)

print(ans)
