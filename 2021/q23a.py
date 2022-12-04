import sys
import codelib as cl

cost = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
col = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
def clear(pos, a, b):
    if a < b:
        return all([pos[c] == '.' for c in range(a+1, b+1)])
    else:
        return all([pos[c] == '.' for c in range(b, a)])
def swap(pos, a, b):
    p = [c for c in pos]
    r = p[a]
    p[a] = p[b]
    p[b] = r
    return ''.join(p)
def adj(pos):
    # OUT -> IN
    for i in range(11):
        if pos[i] != '.':
            c = pos[i]
            if clear(pos, i, col[c]) and pos[9+col[c]] == '.':
                if pos[10+col[c]] == '.':
                    yield (swap(pos, i, 10+col[c]), cost[c]*(abs(i-col[c])+2))
                elif pos[10+col[c]] == c:
                    yield (swap(pos, i, 9+col[c]), cost[c]*(abs(i-col[c])+1))
    # IN -> OUT
    for i in range(11, 19):
        if pos[i] != '.':
            c = pos[i]
            d = ((i-1)//2)*2-8
            if (i%2 == 0 and pos[i-1] != '.') or pos[d] != '.':
                continue
            for g in [0, 1, 3, 5, 7, 9, 10]:
                if clear(pos, d, g):
                    yield (swap(pos, i, g), cost[c]*(abs(d-g)+(2-(i%2))))

grid = []
for line in sys.stdin:
    grid.append(line.rstrip())
spos = grid[1][1:12] + ''.join([grid[i][j] for j in range(3, 10, 2) for i in range(2, 4)])
epos = '.'*11 + 'AABBCCDD'
print(cl.shortest_path_dijkstra(adj, spos, epos))