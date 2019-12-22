import sys

adj = dict()

def dfs(p):
    total = 0
    count = 0
    if p not in adj:
        total = 0
        count = 0
    else:
        for q in adj[p]:
            tot, cnt = dfs(q)
            total += tot
            count += cnt
        total += count
    return (total, count+1)

for line in sys.stdin:
    ea, eb = line.strip().split(')')
    if ea not in adj:
        adj[ea] = []
    adj[ea].append(eb)

z_total, z_count = dfs('COM')
print(z_total)