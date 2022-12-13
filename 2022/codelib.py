import collections
import functools
import heapq


def all_true(*args):
    return True


# ============= Arithmetic

def product(iterable):
    return functools.reduce(lambda x, y: x*y, iterable, 1)


def frequency(iterable):
    d = dict()
    for item in iterable:
        dict_inc(d, item)
    return d


def mod_start1(val, m):
    return ((val-1) % m)+1


def gcd(p, q):
    pp = max(p, q)
    qq = min(p, q)
    while qq != 0:
        rr = pp % qq
        pp = qq
        qq = rr
    return pp


def extended_gcd(p, q):
    rr, r = p, q
    ss, s = 1, 0
    tt, t = 0, 1
    while r != 0:
        qq = rr // r
        rr, r = r, rr-qq*r
        ss, s = s, ss-qq*s
        tt, t = t, tt-qq*t
    return ss, tt


def inverse(p, m):
    v, w = extended_gcd(m, p)
    return w % m


def factorize(n):
    nn = n
    ans = []
    i = 2
    while i*i <= nn:
        if nn % i == 0:
            ans.append(i)
            nn //= i
        else:
            i += 1
    if nn > 1:
        ans.append(nn)
    return ans


# ============= Dictionary helpers


def dict_lambda(d):
    return lambda x: d[x]


def dict_lambda_default(d, default):
    return lambda x: d[x] if x in d else default


def dict_inc(d, key):
    dict_add(d, key, 1)


def dict_add(d, key, val):
    if key not in d:
        d[key] = 0
    d[key] += val


def dict_add_to_list(d, key, item):
    if key not in d:
        d[key] = []
    d[key].append(item)

# ============= Grid helpers


def grid_get_dims(grid):
    return len(grid), len(grid[0])


def grid_coords(grid):
    xh, xw = grid_get_dims(grid)
    for i in range(xh):
        for j in range(xw):
            yield (i, j)


def grid_get(grid, pos):
    i, j = pos
    return grid[i][j]


def grid_set(grid, pos, val):
    i, j = pos
    grid[i][j] = val


def grid_inside(grid_dims, pos):
    i, j = pos
    gridh, gridw = grid_dims
    return 0 <= i < gridh and 0 <= j < gridw


def grid_graph(grid_dims, grid_neighbors, is_edge=all_true, is_node=all_true):
    adj = dict()
    gridh, gridw = grid_dims
    for i in range(gridh):
        for j in range(gridw):
            p = (i, j)
            if not is_node(p):
                continue
            for q in grid_neighbors(grid_dims, p):
                if not is_node(q) or not is_edge(p, q):
                    continue
                dict_add_to_list(adj, p, q)
    return dict_lambda_default(adj, [])


def grid_graph4(grid_dims, is_edge=all_true, is_node=all_true):
    return grid_graph(grid_dims, grid_neighbors4, is_edge, is_node)


def grid_graph8(grid_dims, is_edge=all_true, is_node=all_true):
    return grid_graph(grid_dims, grid_neighbors8, is_edge, is_node)


def grid_wgraph(grid_dims, grid_neighbors, weight_function, is_node=all_true):
    adj = dict()
    gridh, gridw = grid_dims
    for i in range(gridh):
        for j in range(gridw):
            p = (i, j)
            if not is_node(p):
                continue
            for q in grid_neighbors(grid_dims, p):
                if not is_node(q):
                    continue
                w = weight_function(p, q)
                if w is not None:
                    dict_add_to_list(adj, p, (q, w))
    return dict_lambda_default(adj, [])


def grid_wgraph4(grid_dims, weight_function, is_node=all_true):
    return grid_wgraph(grid_dims, grid_neighbors4, weight_function, is_node)


def grid_wgraph8(grid_dims, weight_function, is_node=all_true):
    return grid_wgraph(grid_dims, grid_neighbors8, weight_function, is_node)


def grid_neighbors(grid_dims, pos, neighbor_diffs, is_node=grid_inside):
    i, j = pos
    for di, dj in neighbor_diffs:
        pos_neighbor = (i+di, j+dj)
        if is_node(grid_dims, pos_neighbor):
            yield pos_neighbor


def grid_neighbors4(grid_dims, pos, is_node=grid_inside):
    d = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    return grid_neighbors(grid_dims, pos, d, is_node)


def grid_neighbors8(grid_dims, pos, is_node=grid_inside):
    d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return grid_neighbors(grid_dims, pos, d, is_node)


def grid_print(grid, formatter=str, spacer=''):
    for row in grid:
        print(spacer.join(list(map(formatter, row))))

# ============= Graph algorithms


def reachable_bfs(adj, start):
    visited = set()
    visited.add(start)
    q = collections.deque()
    q.append(start)
    while len(q) > 0:
        p = q.popleft()
        for r in adj(p):
            if r not in visited:
                visited.add(r)
                q.append(r)
    return visited

def shortest_path_bfs(adj, start):
    dist = dict()
    dist[start] = 0
    q = collections.deque()
    q.append(start)
    while len(q) > 0:
        p = q.popleft()
        for r in adj(p):
            if r not in dist:
                dist[r] = dist[p]+1
                q.append(r)
    return dist

def shortest_path_dijkstra(adj, start, end):
    h = []
    dist = {start: 0}
    locked = set()
    heapq.heapify(h)
    heapq.heappush(h, (dist[start], start))
    while len(h) > 0:
        dp, p = heapq.heappop(h)
        if p in locked:
            continue
        locked.add(p)
        for r, d in adj(p):
            if r not in dist or dist[r] > dist[p] + d:
                dist[r] = dist[p] + d
                heapq.heappush(h, (dist[r], r))
    return dist[end]

# ============= Coordinates helpers


def coords_x(coords):
    return list(map(lambda c: c[0], coords))


def coords_y(coords):
    return list(map(lambda c: c[1], coords))


def grid_from_coords(coords, chit='#', cmiss='.'):
    """
        Assumes x goes from left to right, y goes from top to bottom
    """
    cset = set(coords)
    cx = coords_x(coords)
    cy = coords_y(coords)
    minx = min(cx)
    miny = min(cy)
    maxx = max(cx)
    maxy = max(cy)
    grid = []
    for y in range(miny, maxy+1):
        row = []
        for x in range(minx, maxx+1):
            if (x, y) in cset:
                row.append(chit)
            else:
                row.append(cmiss)
        grid.append(row)
    return grid


# ============= Coordinates helpers

class UnionFind:
    def __init__(self):
        self.par = dict()
        self.rnk = dict()

    def union(self, node1, node2):
        n1 = self.find(node1)
        n2 = self.find(node2)
        if self.rnk[n1] > self.rnk[n2]:
            self.par[n2] = n1
        elif self.rnk[n1] < self.rnk[n2]:
            self.par[n1] = n2
        else:
            self.par[n2] = n1
            self.rnk[n1] += 1

    def find(self, node):
        if node not in self.par:
            self.par[node] = node
        if node not in self.rnk:
            self.rnk[node] = 0
        n = node
        while self.par[n] != n:
            n = self.par[n]
        return n

    def is_connected(self, node1, node2):
        return self.find(node1) == self.find(node2)
