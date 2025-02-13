# 시간초과

import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
cpti_list = list(list(input()) for _ in range(n))
re = 0

for comb in combinations(range(n), 2):
    tmp = 0
    for i in range(m):
        if cpti_list[comb[0]][i] != cpti_list[comb[1]][i]:
            tmp += 1

    if tmp <= 2:
        re += 1

print(re)