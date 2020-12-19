import sys

def getNum(getter):
    c = next(getter)
    if c == '(':
        return work(getter)
    else:
        return int(c)

def getSign(getter):
    c = next(getter)
    return c

def work(getter):
    num = getNum(getter)
    sign = getSign(getter)
    while sign != ')':
        num2 = getNum(getter)
        if sign == '+':
            num += num2
        elif sign == '*':
            num *= num2
        sign = getSign(getter)
    return num

ans = 0
for line in sys.stdin:
    inp = line.strip()
    def getter():
        for c in inp:
            if c != ' ':
                yield c
        yield ')'
    ans += work(getter())
print(ans)
