import sys

count = 0
a = 273025
b = 767253
for i in range(a, b+1):
    x = i
    last = None
    fail = False
    same = False
    while x > 0:
        dig = x%10
        x //= 10
        if last is not None and last < dig:
            fail = True
            break
        if last == dig:
            same = True
        last = dig
    if not fail and same:
        count += 1
print(count)