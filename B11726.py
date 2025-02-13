n = int(input())

if n == 1:
    print(1)

elif n == 2:
    print(2)

else :
    dp = [1, 2]
    for _ in range(n-2):
        dp = [dp[1], dp[0]+dp[1]]

    print(dp[1]%10007)