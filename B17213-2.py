# DP 사용
import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())

dp = [[0 for _ in range(M+1)] for _ in range(N)]

for i in range(1, M+1):
    dp[0][i] = 1

for i in range(1, N):
    for j in range(M+1):
        dp[i][j] = 0
        for k in range(1, j+1):
            dp[i][j] += dp[i-1][j-k]

print(dp[N-1][M])