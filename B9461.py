t = int(input())
nums = []
for _ in range(t):
    num = int(input())
    nums.append(num)

mx = max(nums)
dp = [0 for _ in range(101)]
dp[1:6] = [1, 1, 1, 2, 2]

if mx > 5:
    for i in range(6, mx+1):
        dp[i] = dp[i-5] + dp[i-1]

for i in range(t):
    print(dp[nums[i]])