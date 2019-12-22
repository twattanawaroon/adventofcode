import sys

final = [2]*150
for line in sys.stdin:
    x = line.strip()
    for s in range(0, len(x), 150):
        y = x[s:s+150]
        for i in range(150):
            p = int(y[i])
            if final[i] == 2:
                final[i] = p
    for s in range(0, 150, 25):
        y = final[s:s+25]
        print(''.join(map(lambda x: '#' if x == 1 else ' ', y)))