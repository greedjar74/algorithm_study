import sys

n = int(input())
dp = [0 for _ in range(n + 1)]

for i in range(2, n + 1):
    tmp1 = sys.maxsize
    tmp2 = sys.maxsize

    if i % 2 == 0:
        tmp1 = dp[i//2]

    if i % 3 == 0:
        tmp2 = dp[i//3]
    
    dp[i] = min(tmp1, tmp2, dp[i-1]) + 1

print(dp[-1])