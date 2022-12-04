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
            if clear(pos, i, col[c]):
                s = ''.join([pos[2*col[c]+7+k] for k in range(4)])
                if s == '....':
                    yield (swap(pos, i, 2*col[c]+10), cost[c]*(abs(i-col[c])+4))
                elif s == '...'+c:
                    yield (swap(pos, i, 2*col[c]+9), cost[c]*(abs(i-col[c])+3))
                elif s == '..'+c+c:
                    yield (swap(pos, i, 2*col[c]+8), cost[c]*(abs(i-col[c])+2))
                elif s == '.'+c+c+c:
                    yield (swap(pos, i, 2*col[c]+7), cost[c]*(abs(i-col[c])+1))
    # IN -> OUT
    for i in range(11, 27):
        if pos[i] != '.':
            c = pos[i]
            d = ((i-3)//4)*2-2
            if pos[d] != '.' or any([pos[2*d+7+k] != '.' for k in range((i-3)%4)]):
                continue
            for g in [0, 1, 3, 5, 7, 9, 10]:
                if clear(pos, d, g):
                    yield (swap(pos, i, g), cost[c]*(abs(d-g)+((i-3)%4)+1))

grid = []
for line in sys.stdin:
    grid.append(line.rstrip())
grid.insert(3, '  #D#C#B#A#')
grid.insert(4, '  #D#B#A#C#')
spos = grid[1][1:12] + ''.join([grid[i][j] for j in range(3, 10, 2) for i in range(2, 6)])
epos = '.'*11 + 'AAAABBBBCCCCDDDD'
print(cl.shortest_path_dijkstra(adj, spos, epos))