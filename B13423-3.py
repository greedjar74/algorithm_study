# python3 가능
# pypy3 가능
# 그런데 pypy3의 경우 B13423.py와 비교했을 때 오히려 느리다?

import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    nums = list(map(int, input().split()))
    nums.sort()
    S = set(nums)

    cnt = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            if 2 * nums[j] - nums[i] in S:
                cnt += 1

    print(cnt)