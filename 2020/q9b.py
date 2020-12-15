import sys
from collections import deque

def check(nums, num):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == num:
                return True
    return False

def getGoal(x):
    nums = deque()
    for num in x:
        if len(nums) >= 25:
            if not check(nums, num):
                return num
            nums.popleft()
        nums.append(num)

def find(x, goal):
    s = dict([(0, -1)])
    lsum = 0
    for i in range(len(x)):
        lsum += x[i]
        if lsum-goal in s:
            return s[lsum-goal]+1, i+1
        s[lsum] = i

x = []
for line in sys.stdin:
    x.append(int(line.strip()))

goal = getGoal(x)
pi, pj = find(x, goal)
print(max(x[pi: pj])+min(x[pi: pj]))