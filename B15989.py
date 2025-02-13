t = int(input())
nums = []

for _ in range(t):
    num = int(input())
    nums.append(num)

mx_num = max(nums)
dp = [[0 for _ in range(mx_num+1)] for _ in range(4)]
dp[0][0] = 1

for i in range(1, 4):
    for j in range(mx_num+1):
        dp[i][j] = dp[i-1][j]
        
        if j >= i:
            dp[i][j] += dp[i][j-i]

for i in range(t):
    print(dp[3][nums[i]])