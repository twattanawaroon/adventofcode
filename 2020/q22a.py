import sys
from collections import deque

p1 = deque()
p2 = deque()
player = 0
for line in sys.stdin:
    s = line.strip()
    if len(s) == 0:
        continue
    elif s[-1] == ':':
        player += 1
    elif player == 1:
        p1.append(int(s))
    else:
        p2.append(int(s))

while len(p1) > 0 and len(p2) > 0:
    a1 = p1.popleft()
    a2 = p2.popleft()
    if a1 > a2:
        p1.append(a1)
        p1.append(a2)
    else:
        p2.append(a2)
        p2.append(a1)

p = list(p1 if len(p1) > len(p2) else p2)
ans = 0
for i in range(len(p)):
    ans += p[i]*(len(p)-i)
print(ans)
