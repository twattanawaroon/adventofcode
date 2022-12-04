import sys
import codelib as cl

cmdc = 0
r = dict()
for line in sys.stdin:
    cmd = line.strip().split()
    cmdc += 1
    if cmdc % 18 in [5, 6, 16]:
        cl.dict_add_to_list(r, cmdc % 18, int(cmd[2]))
s = []
ans = [None] * 14
for i in range(14):
    c0 = r[5][i]
    c1 = r[6][i]
    c2 = r[16][i]
    if c0 == 1:
        s.append((i, c2))
    else:
        j, c2was = s.pop()
        d = c1+c2was
        for k in range(1, 10):
            l = k+d
            if 1 <= l <= 9:
                ans[j] = k
                ans[i] = l
                break
print(''.join(map(str,ans)))