import sys

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
            ansp += num
    return ansp

mode = 'start'
ans = 0
ranges = dict()
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
    elif mode == 'nearby':
        ans += process(ranges, list(map(int, s.split(','))))
    else:
        t, u = s.split(':')
        ranges[t.strip()] = get_ranges(u.strip())

print(ans)