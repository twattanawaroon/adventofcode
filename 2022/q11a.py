import sys
import codelib as cl

N = 8
l = []
op = []
test = []
xt = []
xf = []
count = [0] * N
for line in sys.stdin:
    s = line.strip()
    if len(s) == 0:
        continue
    cmd, rest = s.split(':')
    cmd = cmd.split()
    rest = rest.strip()
    if cmd[0] == 'Starting':
        l.append(list(map(int, rest.split(', '))))
    elif cmd[0] == 'Operation':
        op.append(rest.split()[-2:])
    elif cmd[0] == 'Test':
        test.append(int(rest.split()[-1]))
    elif cmd[1] == 'true':
        xt.append(int(rest.split()[-1]))
    elif cmd[1] == 'false':
        xf.append(int(rest.split()[-1]))

for r in range(20):
    for monkey in range(N):
        signi, operandi = op[monkey]
        testi = test[monkey]
        xti = xt[monkey]
        xfi = xf[monkey]
        for item in l[monkey]:
            oz = item if operandi == 'old' else int(operandi)
            newitem = (item + oz) if signi == '+' else (item * oz)
            newitem //= 3
            l[xti if newitem % testi == 0 else xfi].append(newitem)
        count[monkey] += len(l[monkey])
        l[monkey].clear()

count.sort()
print(count[-2]*count[-1])
