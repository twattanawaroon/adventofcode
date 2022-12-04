import sys
import codelib as cl
count = 0

def dec(c):
    if 'a' <= c <= 'z':
        return ord(c)-ord('a')+1
    elif 'A' <= c <= 'Z':
        return ord(c)-ord('A')+27
    return None

def freq(v):
    m = dict()
    for i in v:
        cl.dict_inc(m, dec(i))
    return m

for line in sys.stdin:
    u = line.strip()
    s = u[:len(u)//2]
    t = u[len(u)//2:]
    ms = freq(s)
    mt = freq(t)
    for i in range(1, 53):
        if i in ms and i in mt and ms[i] > 0 and mt[i] > 0:
            count += i
            break
print(count)