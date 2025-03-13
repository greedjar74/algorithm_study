import sys
input = sys.stdin.readline
mod = 1000000009

T = int(input().strip())
test_cases = list()
n_max = 0
m_max = 0
for _ in range(T):
    n, m = map(int, input().split())
    n_max = max(n_max, n)
    m_max = max(m_max, m)
    test_cases.append((n, m))

dp = [[0 for _ in range(n_max+1)] for _ in range(m_max+1)]
dp[1][1] = 1
dp[1][2] = 1
dp[1][3] = 1

for i in range(2, m_max+1):
    for j in range(i, n_max+1):
        if i == j:
            dp[i][j] = 1
            continue
        a, b, c = j-1, j-2, j-3
        if a >= 0:
            dp[i][j] += dp[i-1][a]
        if b >= 0:
            dp[i][j] += dp[i-1][b]
        if c >= 0:
            dp[i][j] += dp[i-1][c]
        dp[i][j] %= mod

for test_case in test_cases:
    i, j = test_case
    print(dp[j][i])