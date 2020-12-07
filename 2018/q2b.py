import sys
count2 = 0
count3 = 0

def process(text1, text2):
    s = ''
    for i in range(len(text1)):
        if text1[i] == text2[i]:
            s += text1[i]
    return s if len(s) == len(text1)-1 else None

names = [line for line in sys.stdin]
for i in range(len(names)):
    for j in range(i+1, len(names)):
        ans = process(names[i], names[j])
        if ans is not None:
            print(ans)