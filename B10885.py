import sys
input = sys.stdin.readline

mod = 1000000007

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    A = list(map(int, input().split()))
    dp = [0 for _ in range(N)]
    dp[0] = A[0]
    cnt = [0, 0]
    if A[0] < 0:
        cnt = [1, 0]
    re = dp[0]

    for i in range(1, N):
        if A[i] == 0:
            dp[i] = 0
            cnt = [0, i]
        elif A[i] > 0:
            if dp[i-1] > 0:
                dp[i] = dp[i-1] * A[i]
            else :
                dp[i] = A[i]
        else :
            dp[i] = dp[i-1] * A[i]
            if cnt[0] == 1:
                dp[i] *= dp[cnt[1]]
                cnt = [0, i]
            else :
                cnt = [1, i]

        re = max(re, dp[i])
        
    print(re % mod)