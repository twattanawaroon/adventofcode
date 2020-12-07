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

t = set()
for line in sys.stdin:
    s = line.strip()
    r = solve(s[:-3], 127)
    c = solve(s[-3:], 7)
    i = r*8+c
    t.add(i)

for num in t:
    if num+2 in t and num+1 not in t:
        print(num+1)
