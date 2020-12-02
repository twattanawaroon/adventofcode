import sys
count = 0
for line in sys.stdin:
    rule, s = line.strip().split(':')
    ran, occ = rule.strip().split(' ')
    rana, ranb = ran.strip().split('-')
    if int(rana) <= s.strip().count(occ.strip()) <= int(ranb):
        count += 1
print(count)