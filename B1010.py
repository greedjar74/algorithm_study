def factorial(num):
    re = 1
    for i in range(1, num+1):
        re *= i
    return re

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    re = factorial(m) // (factorial(m-n)*factorial(n))

    print(re)