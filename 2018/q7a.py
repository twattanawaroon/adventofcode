import sys

edgestr = [line.strip() for line in sys.stdin]
edges = {}
indeg = {}
zeroes = []
for i in range(26):
    c = chr(ord('A')+i)
    edges[c] = []
    indeg[c] = 0
for e in edgestr:
    edgespl = e.split()
    p = edgespl[1]
    q = edgespl[7]
    edges[p].append(q)
    indeg[q] += 1
for i in range(26):
    c = chr(ord('A')+i)
    if indeg[c] == 0:
        zeroes.append(c)
ans = ''
while len(zeroes) > 0:
    zeroes.sort()
    zeroes = zeroes[::-1]
    c = zeroes.pop()
    ans += c
    for q in edges[c]:
        indeg[q] -= 1
        if indeg[q] == 0:
            zeroes.append(q)
print(ans)