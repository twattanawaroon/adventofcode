import sys
import codelib as cl
from aocd import submit

count = 0
for line in sys.stdin:
    s = line.strip()
    for i in range(14, len(s)):
        if len(set([c for c in s[i-14:i]])) == 14:
            ansf = i
            break

#print(ansf)
submit(ansf, part="b", day=6, year=2022)