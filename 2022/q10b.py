import sys
import codelib as cl

cmds = []
last = 1
for line in sys.stdin:
    s = line.strip().split()
    if s[0] == 'noop':
        cmds.append(last)
    else:
        cmds.append(last)
        cmds.append(last)
        last += int(s[1])

ans = []
for i in range(len(cmds)):
    c = cmds[i]
    if abs(c - (i % 40)) <= 1:
        ans.append('#')
    else:
        ans.append('.')
    if i % 40 == 39:
        print(''.join(ans))
        ans.clear()
