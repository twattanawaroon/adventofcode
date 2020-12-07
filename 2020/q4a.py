import sys
count = [0]

def process(s):
    t = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    u = set()
    entries = s.split()
    for entry in entries:
        p, q = entry.split(':')
        u.add(p)
    if len(t-u) == 0:
        count[0] += 1

b = ''
for line in sys.stdin:
    s = line.strip()
    if len(s) == 0:
        process(b)
        b = ''
    else:
        b += ' ' + s
process(b)
print(count[0])
