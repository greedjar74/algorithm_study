import sys
input = sys.stdin.readline
mod = 1000000009

N = int(input().strip())
nums = list()
mx = 0
for _ in range(N):
    num = int(input().strip())
    mx = max(mx, num)
    nums.append(num)

dp = [0 for _ in range(mx+1)]
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 2

for i in range(4, mx+1):
    a = i - 2
    b = i - 4
    c = i - 6
    tmp = 0
    if a >= 0:
        tmp += dp[a] % mod
    if b >= 0:
        tmp += dp[b] % mod
    if c >= 0:
        tmp += dp[c] % mod

    dp[i] = tmp

for i in nums:
    print(dp[i]%mod)