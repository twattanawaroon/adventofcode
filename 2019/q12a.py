import sys

def parse(s):
    ans = []
    l = s[1:-1].split(',')
    for item in l:
        ans.append(int(item.split('=')[1]))
    return ans

p = []
v = []

for line in sys.stdin:
    b = line.strip()
    p.append(parse(b))
    v.append([0,0,0])

for timestep in range(1000):
    for dim in range(3):
        for i in range(len(p)):
            for j in range(len(p)):
                if i == j:
                    continue
                if p[i][dim] < p[j][dim]:
                    v[i][dim] += 1
                elif p[i][dim] > p[j][dim]:
                    v[i][dim] -= 1
        for i in range(len(p)):
            p[i][dim] += v[i][dim]
tot = 0
for i in range(len(p)):
    tot += sum(map(abs,p[i]))*sum(map(abs,v[i]))
print(tot)