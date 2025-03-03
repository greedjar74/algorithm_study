import sys
input = sys.stdin.readline

N = int(input().strip())
nums = list(map(int, input().split()))

dp = [0 for _ in range(N)]
mn = nums[0]

for i in range(1, N):
    tmp = nums[i] - mn
    dp[i] = max(tmp, dp[i-1])
    mn = min(mn, nums[i])

print(*dp)