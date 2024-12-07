import sys
import codelib as cl

count = 0
for line in sys.stdin:
    s, t = line.strip().split(',')
    s1, s2 = map(int, s.split('-'))
    t1, t2 = map(int, t.split('-'))
    if (s1 <= t1 and t2 <= s2) or (t1 <= s1 and s2 <= t2):
        count += 1
print(count)
