# 시간초과 발생

import sys
input = sys.stdin.readline

def find_idx(nums, num):
    left, right = 0, len(nums)-1
    while left < right:
        m = (left + right) // 2
        if nums[m] >= num:
            right = m
        else :
            left = m+1

    return (left + right) // 2

m, n = map(int, input().split())
nums = list(int(input().strip()) for _ in range(n))
nums.sort()

while True:
    mx = nums[-1]
    s_idx = find_idx(nums, mx)
    k = n - s_idx
    if k < m:
        nums[s_idx:] = [mx-1 for _ in range(k)]
        m -= k
    else :
        nums[s_idx:s_idx+m] = [mx-1 for _ in range(m)]
        break

re = 0
for i in range(n):
    re += (nums[i] ** 2)

print(re % (2**64))