import sys
from collections import deque

class Unit(object):
    def __init__(self):
        self.hp = 200
        self.atk = 3

    def setXY(self, _x, _y):
        self.x = _x
        self.y = _y

    def adjacent(self, u):
        return (self.x == u.x and abs(self.y-u.y) == 1) or (self.y == u.y and abs(self.x-u.x) == 1)

class Goblin(Unit):
    def isLivingEnemy(self, u):
        return isinstance(u, Elf) and u.hp > 0

    def __str__(self):
        return 'G'

class Elf(Unit):
    def isLivingEnemy(self, u):
        return isinstance(u, Goblin) and u.hp > 0

    def __str__(self):
        return 'E'

def getObj(c):
    if c == 'E':
        return Elf()
    elif c == 'G':
        return Goblin()
    else:
        return c

def getEnemyKey(unit):
    return (unit.hp, unit.x, unit.y)

def getUnits(grid):
    units = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if isinstance(grid[i][j], Unit) and grid[i][j].hp > 0:
                units.append(grid[i][j])
    return units

def getEnemies(units, unit):
    return list(filter(unit.isLivingEnemy, units))

def inRange(enemies, unit):
    return any(map(unit.adjacent, enemies))

def bfs(grid, start, isGoalMarker):
    q = deque()
    dist = dict()
    q.append(start)
    dist[start] = 0
    foundDist = None
    foundCand = None
    dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    while len(q) > 0:
        fx, fy = q.popleft()
        if foundDist is not None and dist[(fx, fy)] > foundDist:
            break
        for dx, dy in dirs:
            gx = fx+dx
            gy = fy+dy
            if isGoalMarker(unit, grid[gx][gy]) and (foundCand is None or (fx, fy) < foundCand):
                foundDist = dist[(fx, fy)]
                foundCand = (fx, fy)
            if grid[gx][gy] == '.' and (gx, gy) not in dist:
                dist[(gx, gy)] = dist[(fx, fy)]+1
                q.append((gx, gy))
    return foundCand

def getBestGoal(grid, unit):
    def isGoalMarker(u, marker):
        return u.isLivingEnemy(marker)
    return bfs(grid, (unit.x, unit.y), isGoalMarker)

def getBestMovement(grid, unit, hx, hy):
    def isGoalMarker(u, marker):
        return marker == unit
    return bfs(grid, (hx, hy), isGoalMarker)

def getBestAdjEnemy(enemies, unit):
    adjEnemies = filter(unit.adjacent, enemies)
    return min(adjEnemies, key=getEnemyKey, default=None)

def getTotalHp(grid):
    units = getUnits(grid)
    return sum(map(lambda unit: unit.hp, units))

grid = []

b = ''
for line in sys.stdin:
    grid.append([getObj(c) for c in line.strip()])

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if isinstance(grid[i][j], Unit):
            grid[i][j].setXY(i, j)

rounds = 0
done = False
while True:
    units = getUnits(grid)
    for unit in units:
        if unit.hp <= 0:
            continue
        enemies = getEnemies(units, unit)
        if len(enemies) == 0:
            done = True
            break
        if not inRange(enemies, unit):
            h = getBestGoal(grid, unit)
            if h is not None:
                hx, hy = h
                bx, by = getBestMovement(grid, unit, hx, hy)
                grid[bx][by] = unit
                grid[unit.x][unit.y] = '.'
                unit.x = bx
                unit.y = by
        bestAdjEnemy = getBestAdjEnemy(enemies, unit)
        if bestAdjEnemy is not None:
            bestAdjEnemy.hp -= unit.atk
            if bestAdjEnemy.hp <= 0:
                grid[bestAdjEnemy.x][bestAdjEnemy.y] = '.'
    if done:
        break
    rounds += 1

totalHp = getTotalHp(grid)
print(rounds*totalHp)
