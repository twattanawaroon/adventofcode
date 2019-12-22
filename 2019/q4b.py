import sys

count = 0
a = 273025
b = 767253
for z in range(a, b+1):
    x = z
    last = None
    fail = False
    match = False
    y = []
    while x > 0:
        dig = x%10
        x //= 10
        y.append(dig)
    for i in range(len(y)-1):
        if y[i] < y[i+1]:
            fail = True
    for i in range(len(y)-1):
        if y[i] == y[i+1] and (i+2 >= len(y) or y[i]!=y[i+2]) and (i == 0 or y[i] != y[i-1]):
            match = True
    if (not fail) and match:
        count += 1
print(count)