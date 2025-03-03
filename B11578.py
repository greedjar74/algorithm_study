from itertools import combinations

N, M = map(int, input().split())
A = list(list(map(int, input().split()))[1:] for _ in range(M))
A = list(set(a) for a in A)

re = -1
for n in range(1, M+1):
    found = False
    for comb in combinations(A, n):
        U = set()
        for a in comb:
            U |= a
        if len(list(U)) == N:
            found = True
            break
    if found:
        re = n
        break

print(re)