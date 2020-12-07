import sys

inps = []
rules = dict()
def process(text):
    if text.count('initial') > 0:
        p, q = text.split(':')
        inps.append(q.strip())
    elif text.count('=>') > 0:
        p, q = text.split('=>')
        rules[p.strip()] = q.strip()

for line in sys.stdin:
    process(line)

for inp in inps:
    n = len(inp)*5
    off = len(inp)*2
    curr = '.'*off + inp + '.'*off
    for gen in range(150):
        x = []
        for i in range(n):
            if 2 <= i < n-2 and curr[i-2:i+3] in rules:
                x.append(rules[curr[i-2:i+3]])
            else:
                x.append('.')
        curr = ''.join(x)
        ans = 0
        for i in range(n):
            if curr[i] == '#':
                ans += i-off
        print(curr, gen+1, ans, 80*(gen+1))
    print(80*50000000000)