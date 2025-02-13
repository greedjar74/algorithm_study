# 풀이 참조함

n = int(input())
nums = list(map(int, input().split()))
k = int(input())
nums.insert(0, 0)

dp = [[0 for _ in range(4)] for _ in range(n+1)]

for j in range(1, 4):
    for i in range(1, n+1):
        if i <= k*j:
            dp[i][j] = sum(nums[:i+1])
        else :
            dp[i][j] = max(dp[i-1][j], sum(nums[i-k+1:i+1])+dp[i-k][j-1])

print(dp[-1][-1])