import sys
import codelib as cl

val = dict()
exp = dict()
for line in sys.stdin:
    var, exps = line.strip().split(': ')
    expz = exps.split()
    if len(expz) == 1:
        if var == 'humn':
            val[var] = None
        else:
            val[var] = int(expz[0])
    else:
        if var == 'root':
            expz[1] = '-'
        exp[var] = tuple(expz)


def find(name):
    if name in val:
        return val[name]
    else:
        sa, o, sb = exp[name]
        a = find(sa)
        b = find(sb)
        if a is None or b is None:
            return None
        val[name] = cl.arithmetic(a, b, o)
        return val[name]


def solve(name, goal):
    val[name] = goal
    if name != 'humn':
        sa, o, sb = exp[name]
        a = val[sa] if sa in val else None
        b = val[sb] if sb in val else None
        if a is None:
            if o == '+':
                ans = goal-b
            elif o == '-':
                ans = goal+b
            elif o == '*':
                ans = goal//b
            else:
                ans = goal*b
            solve(sa, ans)
        else:
            if o == '+':
                ans = goal-a
            elif o == '-':
                ans = a-goal
            elif o == '*':
                ans = goal//a
            else:
                ans = a//goal
            solve(sb, ans)


find('root')
solve('root', 0)
print(val['humn'])
