# 수학적 사고력 필요

import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
re = 1
for i in range(1, M-N+1):
    re *= (M-i)
    re //= i
print(re)