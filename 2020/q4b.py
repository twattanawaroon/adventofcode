import sys
count = [0]

def valid(p, q):
    if p == 'byr':
        return q.isnumeric() and 1920 <= int(q) <= 2002
    elif p == 'iyr':
        return q.isnumeric() and 2010 <= int(q) <= 2020
    elif p == 'eyr':
        return q.isnumeric() and 2020 <= int(q) <= 2030
    elif p == 'hgt':
        if q.endswith('cm'):
            return q[:-2].isnumeric() and 150 <= int(q[:-2]) <= 193
        elif q.endswith('in'):
            return q[:-2].isnumeric() and 59 <= int(q[:-2]) <= 76
        else:
            return False
    elif p == 'hcl':
        return len(q) == 7 and q[0] == '#' and all([c in '0123456789abcdef' for c in q[1:]])
    elif p == 'ecl':
        return q in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif p == 'pid':
        return len(q) == 9 and q.isnumeric()
    else:
        return False

def process(s):
    t = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    u = set()
    entries = s.split()
    for entry in entries:
        p, q = entry.split(':')
        if valid(p, q):
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
