n = int(input())
weights = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

dp = [[False for _ in range(40001)] for _ in range(n)]

for i in range(n):
    current = weights[i]
    dp[i][current] = True # 추 자기자신의 무게는 항상 구현가능

    for j in range(40001):
        if not dp[i-1][j]: # dp[i-1][j]가 구현 불가능하므로 j무게를 활용한 다른 값도 구현 불가능
            continue
        dp[i][j] = True # dp[i-1][j]가 가능하므로 current와 상관없이 dp[i][j]는 항상 가능하다.
        dp[i][abs(j-current)] = True # dp[i-1][j]가 가능하므로 j와 current값의 차이만큼도 구현가능하다. -> 4, 7 두 개의 추가 있으면 무게 3도 구현가능한 것!
        dp[i][j + current] = True # dp[i-1][j]가 가능하므로 j에 current를 더한 값도 구현가능하다.

for num in nums:
    if dp[n-1][num]:
        print("Y", end=' ')
    else :
        print("N", end=" ")