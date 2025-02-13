n, m = map(int, input().split())

if n >= m: # n이 m보다 큰 경우 n!에 m이 포함되므로 나머지는 0이 된다.
    print(0)

else :
    re = 1
    for i in range(1, n+1):
        re *= i
        re %= m
    print(re)