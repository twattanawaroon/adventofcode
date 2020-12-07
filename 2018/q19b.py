import sys

def parse(strin):
    return map(int, ((strin.split('[')[1]).split(']')[0]).split(','))

def addr(x, a, b, c):
    y = list(x)
    y[c] = y[a]+y[b]
    return tuple(y)

def addi(x, a, b, c):
    y = list(x)
    y[c] = y[a]+b
    return tuple(y)

def mulr(x, a, b, c):
    y = list(x)
    y[c] = y[a]*y[b]
    return tuple(y)

def muli(x, a, b, c):
    y = list(x)
    y[c] = y[a]*b
    return tuple(y)

def banr(x, a, b, c):
    y = list(x)
    y[c] = y[a]&y[b]
    return tuple(y)

def bani(x, a, b, c):
    y = list(x)
    y[c] = y[a]&b
    return tuple(y)

def borr(x, a, b, c):
    y = list(x)
    y[c] = y[a]|y[b]
    return tuple(y)

def bori(x, a, b, c):
    y = list(x)
    y[c] = y[a]|b
    return tuple(y)

def setr(x, a, b, c):
    y = list(x)
    y[c] = y[a]
    return tuple(y)

def seti(x, a, b, c):
    y = list(x)
    y[c] = a
    return tuple(y)

def gtir(x, a, b, c):
    y = list(x)
    y[c] = 1 if a > y[b] else 0
    return tuple(y)

def gtri(x, a, b, c):
    y = list(x)
    y[c] = 1 if y[a] > b else 0
    return tuple(y)

def gtrr(x, a, b, c):
    y = list(x)
    y[c] = 1 if y[a] > y[b] else 0
    return tuple(y)

def eqir(x, a, b, c):
    y = list(x)
    y[c] = 1 if a == y[b] else 0
    return tuple(y)

def eqri(x, a, b, c):
    y = list(x)
    y[c] = 1 if y[a] == b else 0
    return tuple(y)

def eqrr(x, a, b, c):
    y = list(x)
    y[c] = 1 if y[a] == y[b] else 0
    return tuple(y)

ops = [addi, bani, gtir, borr, eqrr, bori, gtrr, setr, muli, seti, banr, gtri, eqir, eqri, addr, mulr]
opmap = dict()
for op in ops:
    opmap[op.__name__] = op

instrs = []
for line in sys.stdin:
    inp = line.strip()
    if inp.startswith('#ip'):
        jnk, ipl = inp.split()
        ipc = int(ipl)
    else:
        oo, aa, bb, cc = inp.split()
        instrs.append((opmap[oo], int(aa), int(bb), int(cc)))

x = [1] + [0]*5
ip = 0
while ip < len(instrs):
    if ip == 1:
        break
    x[ipc] = ip
    oo, aa, bb, cc = instrs[ip]
    x = list(oo(x, aa, bb, cc))
    ip = x[ipc]+1

ans = 0
i = 1
n = x[2]
while i*i <= n:
    if n % i == 0:
        j = n//i
        ans += i
        if i != j:
            ans += j
    i += 1
print(ans)