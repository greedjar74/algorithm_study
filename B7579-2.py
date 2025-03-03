# dp[i][j]는 j이하의 비용으로 i이하의 앱들 중 일부를 제거해서 만들 수 있는 최대의 메모리

import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

dp = [[0 for _ in range(10001)] for _ in range(N)]

# dp[0][i]
# if i < C[0]: 종료할 수 없다.
# if i >= C[0]: M[0]만큼 메모리를 확보할 수 있다.
for i in range(C[0], 10001):
    dp[0][i] = A[0]

for i in range(1, N):
    for j in range(10001):
        dp[i][j] = dp[i-1][j]
        if j >= C[i]:
            dp[i][j] = max(dp[i][j], A[i] + dp[i-1][j-C[i]])

for i in range(10001):
    if dp[N-1][i] >= M:
        print(i)
        break