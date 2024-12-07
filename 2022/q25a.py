import sys
import codelib as cl

chart = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
chart_rev = '012=-'


def to_dec(num):
    val = 0
    for digit in num:
        val *= 5
        val += chart[digit]
    return val


def to_snafu(num):
    num_string = []
    while num != 0:
        c = chart_rev[num % 5]
        num_string.append(c)
        num -= chart[c]
        num //= 5
    return ''.join(num_string[::-1])


nums = []
for line in sys.stdin:
    nums.append(line.strip())

print(to_snafu(sum(map(to_dec, nums))))
