n = int(input())
nums = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(1, n):
    mx = 0
    for j in range(i):
        if nums[j] < nums[i] and mx < dp[j]:
            mx = dp[j]

    dp[i] = mx + 1

print(max(dp))