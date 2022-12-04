import sys
import codelib as cl

x = [7, 9]
sc = [0, 0]
turn = 0
rolls = 0
d = 1
while True:
    s = 0
    for t in range(3):
        rolls += 1
        s += d
        d = cl.mod_start1(d+1, 100)
    x[turn] = cl.mod_start1(x[turn]+s, 10)
    sc[turn] += x[turn]
    if sc[turn] > 1000:
        print(sc[1-turn]*rolls)
        break
    turn = 1-turn
