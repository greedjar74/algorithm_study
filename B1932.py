n = int(input())
pyramid = list()

for _ in range(n):
    nums = list(map(int, input().split()))
    pyramid.append(nums)

dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = pyramid[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + pyramid[i][0]

        elif j == i:
            dp[i][j] = dp[i-1][j-1] + pyramid[i][j]

        else :
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + pyramid[i][j]

print(max(dp[-1]))