n = int(input())
points = list()
for _ in range(n):
    point = int(input())
    points.append(point)
points.insert(0, 0)

dp = [0 for _ in range(n+1)]

if n == 1:
    dp[1] = points[1]
    print(dp[1])

elif n == 2:
    dp[1] = points[1]
    dp[2] = points[1]+points[2]
    print(dp[2])

else :
    dp[1] = points[1]
    dp[2] = points[1]+points[2]
    for i in range(3, n+1):
        dp[i] = max(dp[i-3]+points[i-1]+points[i], dp[i-2]+points[i])

    print(dp[-1])