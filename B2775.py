t = int(input())
k_list = []
n_list = []

for _ in range(t):
    k = int(input())
    n = int(input())
    k_list.append(k)
    n_list.append(n)

k_mx = max(k_list)
n_mx = max(n_list)

dp = [[0 for _ in range(n_mx+1)] for _ in range(k_mx+1)]

for k in range(k_mx+1):
    for n in range(1, n_mx+1):
        if k == 0:
            dp[k][n] = n
        
        elif n == 1:
            dp[k][n] = 1

        else :
            dp[k][n] = dp[k][n-1] + dp[k-1][n]

for i in range(t):
    print(dp[k_list[i]][n_list[i]])