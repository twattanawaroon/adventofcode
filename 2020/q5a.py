import sys

def solve(s, r):
    l = 0
    for c in s:
        m = (l+r)//2
        if c == 'F' or c == 'L':
            r = m
        else:
            l = m+1
    return l

ans = None
for line in sys.stdin:
    s = line.strip()
    r = solve(s[:-3], 127)
    c = solve(s[-3:], 7)
    i = r*8+c
    if ans is None or i > ans:
        ans = i
print(ans)