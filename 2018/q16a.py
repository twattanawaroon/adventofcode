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

ops = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

ans = 0
for i in range(776):
    x = tuple(parse(input().strip()))
    y = tuple(map(int, input().strip().split()))
    z = tuple(parse(input().strip()))
    input()
    pas = 0
    for op in ops:
        opc, aa, bb, cc = y
        if op(x, aa, bb, cc) == z:
            pas += 1
    if pas >= 3:
        ans += 1
print(ans)
