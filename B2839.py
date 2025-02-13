n = int(input())
re = 0

while n >= 0:
    if n % 5 == 0:
        re += n // 5
        print(re)
        exit(0)

    n -= 3
    re += 1

print(-1)