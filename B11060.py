import sys

n = int(input())
nums = list(map(int, input().split()))
dp = [sys.maxsize for _ in range(n)]
possible = [False for _ in range(n)]
dp[0] = 0
possible[0] = True

for i in range(n):
    if possible[i]:
        tmp = i + nums[i]
        for j in range(i, tmp+1):
            if j < n:
                dp[j] = min(dp[j], dp[i] + 1)
                possible[j] = True

if possible[-1]:
    print(dp[-1])
else :
    print(-1)