import sys

cmds = []
for line in sys.stdin:
    ins, val = line.strip().split()
    cmds.append((ins, int(val)))

def eval(cmds):
    done = set()
    num = 0
    val = 0
    while num not in done and num < len(cmds):
        done.add(num)
        ins, v = cmds[num]
        if ins == 'jmp':
            num += v
        elif ins == 'acc':
            val += v
            num += 1
        else:
            num += 1
    if num == len(cmds):
        return val
    else:
        return None

for i in range(len(cmds)):
    if cmds[i][0] == 'jmp':
        cmds[i] = ('nop', cmds[i][1])
        x = eval(cmds)
        if x is not None:
            print(x)
        cmds[i] = ('jmp', cmds[i][1])
    if cmds[i][0] == 'nop':
        cmds[i] = ('jmp', cmds[i][1])
        x = eval(cmds)
        if x is not None:
            print(x)
        cmds[i] = ('nop', cmds[i][1])
