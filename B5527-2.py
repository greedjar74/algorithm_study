# DP활용

import sys
input = sys.stdin.readline

N = int(input().strip())
lights = list(map(int, input().split()))

D = [0 for _ in range(N)]
E = [0 for _ in range(N)]
F = [0 for _ in range(N)]

D[0] = E[0] = F[0] = 1

for i in range(1, N):
    if lights[i] == lights[i-1]:
        D[i] = 1
        E[i] = D[i-1] + 1
        F[i] = E[i-1] + 1

    else :
        D[i] = D[i-1] + 1
        E[i] = E[i-1] + 1
        F[i] = F[i-1] + 1

print(max(max(D), max(E), max(F)))