import sys
from networkx.algorithms import bipartite as bp
from scipy.sparse import lil_matrix

def get_ranges(s):
    ranges_raw = s.split('or')
    p = []
    for u in ranges_raw:
        p.append(tuple(map(int, u.strip().split('-'))))
    return p

def valid(ranges, num):
    for a, b in ranges:
        if a <= num <= b:
            return True
    return False

def process(ranges, nums):
    ansp = 0
    for num in nums:
        if not any([valid(ranges[c], num) for c in ranges]):
            return False
    return True

mode = 'start'
ranges = dict()
your_ticket = None
tks = []
for line in sys.stdin:
    s = line.strip()
    if len(s) == 0:
        continue
    elif s.startswith('your'):
        mode = 'your'
    elif s.startswith('nearby'):
        mode = 'nearby'
    elif mode == 'your':
        your_ticket = list(map(int, s.split(',')))
        tks.append(your_ticket)
    elif mode == 'nearby':
        ticket = list(map(int, s.split(',')))
        if process(ranges, ticket):
            tks.append(ticket)
    else:
        t, u = s.split(':')
        ranges[t.strip()] = get_ranges(u.strip())

fields = list(ranges.keys())
mtx = []
for field in fields:
    y = []
    for i in range(len(your_ticket)):
        v = all([valid(ranges[field], tk[i]) for tk in tks])
        y.append(1 if v else 0)
    mtx.append(y)

g = bp.matrix.from_biadjacency_matrix(lil_matrix(mtx))
matching = bp.matching.maximum_matching(g)

ans = 1
for i in range(len(fields)):
    if fields[i].startswith('departure'):
        slot = matching[i]-len(fields)
        ans *= your_ticket[slot]
print(ans)