import sys
from collections import deque

def check(nums, num):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == num:
                return True
    return False

nums = deque()
for line in sys.stdin:
    num = int(line.strip())
    if len(nums) >= 25:
        if not check(nums, num):
            print(num)
            break
        nums.popleft()
    nums.append(num)
