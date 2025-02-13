n = int(input())
dp = [False, True, False, True, True]

if n < 5:
    if dp[n]:
        print("SK")
    else :
        print("CY")

else :
    for i in range(5, n+1):
        a, b, c = i-1, i-3, i-4
        if dp[a] and dp[b] and dp[c]:
            dp.append(False)
        else :
            dp.append(True)

    if dp[n]:
        print("SK")
    else :
        print("CY")