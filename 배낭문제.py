n = int(input())
weights = list(map(int, input().split()))
weights.insert(0, 0)
prices = list(map(int, input().split()))
prices.insert(0, 0)
W = int(input())

dp = [[0 for _ in range(W+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for w in range(W+1):
        if w < weights[i]:
            dp[i][w] = dp[i-1][w]

        else :
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i]]+prices[i])

print(dp[-1][-1])