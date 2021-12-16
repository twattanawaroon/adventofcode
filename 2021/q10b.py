import sys
from collections import deque

c = {'(': ')', '[': ']', '{': '}', '<': '>'}
s = {'(': 1, '[': 2, '{': 3, '<': 4}

scores = []
for line in sys.stdin:
    x = line.strip()
    q = deque()
    fail = False
    for item in x:
        if item in c:
            q.append(item)
        else:
            if len(q) == 0 or c[q.pop()] != item:
                fail = True
                break
    if not fail:
        sc = 0
        while len(q) > 0:
            sc *= 5
            sc += s[q.pop()]
        scores.append(sc)

scores.sort()
print(scores[len(scores)//2])
