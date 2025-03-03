# 메모리 초과 발생
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
B = []
for i in range(N):
    B.append((A[i], C[i]))

B.sort(key= lambda x: x[0])
A.sort()
A.insert(0, 0)
B.insert(0, (0, 0))

dp = [[INF for _ in range(M+1)] for _ in range(N)]

for i in range(N):
    for j in range(M+1):
        if j == 0:
            dp[i][j] = 0
        elif sum(A[:i+1]) < j:
            dp[i][j] = INF
        else :
            tmp = sum(A[:i])
            if tmp < j <= A[i]:
                dp[i][j] = B[i][1]
            else :
                dp[i][j] = min(dp[i-1][j], B[i][1] + dp[i-1][j-A[i]])

print(dp[-1][-1])