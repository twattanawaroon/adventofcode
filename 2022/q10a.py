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

ansf = 0
for i in range(19, len(cmds), 40):
    ansf += (i + 1) * cmds[i]
print(ansf)
