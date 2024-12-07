import sys
import codelib as cl

count = 0


def dec(c):
    if 'a' <= c <= 'z':
        return ord(c) - ord('a') + 1
    elif 'A' <= c <= 'Z':
        return ord(c) - ord('A') + 27
    return None


def freq(v):
    m = dict()
    for i in v:
        cl.dict_inc(m, dec(i))
    return m


ms = []
for line in sys.stdin:
    u = line.strip()
    ms.append(freq(u))
    if len(ms) == 3:
        for i in range(1, 53):
            if all([i in m and m[i] > 0 for m in ms]):
                count += i
                break
        ms.clear()
print(count)
