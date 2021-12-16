import sys
from collections import deque

c = {'(': ')', '[': ']', '{': '}', '<': '>'}
s = {')': 3, ']': 57, '}': 1197, '>': 25137}

score = 0
for line in sys.stdin:
    x = line.strip()
    q = deque()
    for item in x:
        if item in c:
            q.append(item)
        else:
            if len(q) == 0 or c[q.pop()] != item:
                score += s[item]
                break

print(score)
