import sys

ings = set()
algs = set()
c = []
for line in sys.stdin:
    s = line.strip()[:-1]
    s1, s2 = s.split('(contains ')
    x = set(s1.strip().split())
    y = set(s2.strip().split(', '))
    c.append((x, y))

for x, y in c:
    ings |= x
    algs |= y

m = dict()
for alg in algs:
    m[alg] = ings.copy()

for x, y in c:
    for alg in y:
        m[alg] &= x

safe_ings = ings.copy()
for alg in algs:
    safe_ings -= m[alg]

print(sum([len(safe_ings & x) for x, y in c]))
