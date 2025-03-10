import sys
input = sys.stdin.readline

D, K = map(int, input().split())

a = [0, 1]
b = [1, 1]

if D > 3:
    for _ in range(4, D+1):
        a = [a[1], a[0] + a[1]]
        b = [b[1], b[0] + b[1]]

re = 1
while True:
    tmp = K - re * a[1]
    if tmp % b[1] == 0:
        print(re)
        print(tmp//b[1])
        break
    re += 1