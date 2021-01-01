import sys
MD = 20201227

def get_exp(keys):
    e = 0
    num = 1
    while True:
        num *= 7
        num %= MD
        e += 1
        for i in range(2):
            if num == keys[i]:
                return e, i

def my_pow(p, e):
    ans = 1
    for i in range(e):
        ans *= p
        ans %= MD
    return ans

keys = []
for line in sys.stdin:
    s = line.strip()
    keys.append(int(s))

e, which = get_exp(keys)
print(my_pow(keys[1-which], e))
