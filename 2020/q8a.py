import sys

cmds = []
for line in sys.stdin:
    ins, val = line.strip().split()
    cmds.append((ins, int(val)))

done = set()
num = 0
val = 0
while num not in done:
    done.add(num)
    ins, v = cmds[num]
    if ins == 'jmp':
        num += v
    elif ins == 'acc':
        val += v
        num += 1
    else:
        num += 1

print(val)
