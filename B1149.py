import sys
INF = sys.maxsize

n = int(input())
cost_list = []
for _ in range(n):
    costs = list(map(int, input().split()))
    cost_list.append(costs)

dp = [[INF for _ in range(n+1)] for _ in range(3)]
dp[0][0] = 0
dp[1][0] = 0
dp[2][0] = 0

for j in range(1, n+1):
    for i in range(3):
        for k in range(3):
            if i != k:
                dp[i][j] = min(dp[i][j], dp[k][j-1]+cost_list[j-1][i])

print(min(dp[0][-1], dp[1][-1], dp[2][-1]))