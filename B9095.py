t = int(input())
nums = []

for _ in range(t):
    nums.append(int(input()))
    
n = max(nums)
dp = [0 for _ in range(n + 1)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, n+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(t):
    print(dp[nums[i]])