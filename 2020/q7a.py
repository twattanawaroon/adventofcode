import sys
from collections import deque

def get_color(s):
    return s.strip()[:-4].strip()

adj = dict()
for line in sys.stdin:
    s, t = line.strip()[:-1].split('contain')
    treqs = t.split(',')
    sc = get_color(s)
    for treq in treqs:
        tn, ttc = treq.strip().split(' ', 1)
        tc = get_color(ttc)
        if tc not in adj:
            adj[tc] = set()
        adj[tc].add((sc, tn))

start = 'shiny gold'
found = dict()
found[start] = True
q = deque()
q.append(start)
ans = 0
while len(q) > 0:
    p = q.pop()
    ans += 1
    if p not in adj:
        continue
    for r, cr in adj[p]:
        if r not in found:
            found[r] = True
            q.append(r)

print(ans-1)
