import sys
import codelib as cl

val = dict()
exp = dict()
for line in sys.stdin:
    var, exps = line.strip().split(': ')
    expz = exps.split()
    if len(expz) == 1:
        val[var] = int(expz[0])
    else:
        exp[var] = tuple(expz)


def find(name):
    if name in val:
        return val[name]
    else:
        sa, o, sb = exp[name]
        a = find(sa)
        b = find(sb)
        val[name] = cl.arithmetic(a, b, o)
        return val[name]


print(find('root'))
