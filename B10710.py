n, m = map(int, input().split())
D = [int(input()) for _ in range(n)]
C = [int(input()) for _ in range(m)]

dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
for i in range(1, m+1):
    for j in range(1, n+1):
        if i == j:
            dp[i][j] = dp[i-1][j-1] + C[i-1]*D[j-1]
        elif j < i:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]+C[i-1]*D[j-1])

print(dp[-1][-1])