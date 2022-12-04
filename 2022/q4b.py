import sys
count = 0
for line in sys.stdin:
    s, t = line.strip().split(',')
    s1, s2 = map(int, s.split('-'))
    t1, t2 = map(int, t.split('-'))
    if not (t2 < s1 or s2 < t1):
        count += 1
print(count)