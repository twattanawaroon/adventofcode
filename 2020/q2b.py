import sys
count = 0
for line in sys.stdin:
    rule, s = line.strip().split(':')
    ran, occ = rule.strip().split(' ')
    rana, ranb = ran.strip().split('-')
    p = s.strip()[int(rana)-1]
    q = s.strip()[int(ranb)-1]
    if (p == occ and q != occ) or (p != occ and q == occ):
        count += 1
print(count)