# dp로 풀었음 -> 근데 굳이 dp를 안 해도 됨

n = int(input())
pc_list = list(tuple(map(int, input().split())) for _ in range(n))
dp = [[0 for _ in range(n+1)] for _ in range(2)]

for i in range(1, n+1):
    p, c = pc_list[i-1]
    tmp1 = dp[0][i-1]
    tmp2 = dp[0][i-1]
    
    if abs(tmp1-p) <= c:
        tmp1 += 1
    if abs(tmp2-p) <= c:
        tmp2 += 1

    dp[0][i] = max(tmp1, tmp2)
    dp[1][i] = max(dp[0][i-1], dp[1][i-1])

print(max(dp[0][n], dp[1][n]))