import sys
import codelib as cl

freq = dict()
temp = dict()
pair = dict()
for line in sys.stdin:
    s = line.strip()
    if len(s) > 0 and '-' in s:
        a, b = s.split(' -> ')
        temp[a] = b
    elif len(s) > 0:
        for i in range(len(s)-1):
            cl.dict_inc(pair, (s[i], s[i+1]))
        for i in range(len(s)):
            cl.dict_inc(freq, s[i])

for step in range(40):
    pnew = dict()
    for a, b in pair:
        j = temp[a+b]
        cl.dict_add(pnew, (a, j), pair[(a, b)])
        cl.dict_add(pnew, (j, b), pair[(a, b)])
        cl.dict_add(freq, j, pair[(a, b)])
    pair = pnew

fs = [freq[item] for item in freq]
fs.sort()

print(fs[-1]-fs[0])
