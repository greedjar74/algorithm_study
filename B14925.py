import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(N))
dp = [[0 for _ in range(M)] for _ in range(N)]

re = 0
for i in range(N-1, -1, -1):
    for j in range(M-1, -1, -1):
        if board[i][j] != 0:
            continue
        if i == N-1 or j == M-1:
            dp[i][j] = 1
            re = max(re, dp[i][j])
            continue
        if dp[i+1][j] == dp[i][j+1]:
            if board[i+dp[i+1][j]][j+dp[i+1][j]] == 0:
                dp[i][j] = dp[i+1][j] + 1
            else :
                dp[i][j] = dp[i+1][j]
        else :
            dp[i][j] = min(dp[i+1][j]+1, dp[i][j+1]+1)
        
        re = max(re, dp[i][j])

print(re)