import sys
from collections import deque

def make_copy(p, a):
    i = 0
    x = deque()
    for item in p:
        x.append(item)
        i += 1
        if i >= a:
            return x

def play(p1, p2):
    states = set()
    while len(p1) > 0 and len(p2) > 0:
        state = (tuple(p1), tuple(p2))
        if state in states:
            return 1, []
        states.add(state)
        a1 = p1.popleft()
        a2 = p2.popleft()
        if a1 <= len(p1) and a2 <= len(p2):
            q1 = make_copy(p1, a1)
            q2 = make_copy(p2, a2)
            winner = play(q1, q2)[0]
        else:
            winner = 1 if a1 > a2 else 2
        if winner == 1:
            p1.append(a1)
            p1.append(a2)
        else:
            p2.append(a2)
            p2.append(a1)
    if len(p1) > len(p2):
        return 1, p1
    else:
        return 2, p2

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

r = play(p1, p2)[1]
p = list(r)
ans = 0
for i in range(len(p)):
    ans += p[i]*(len(p)-i)
print(ans)
