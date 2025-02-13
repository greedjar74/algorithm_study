from itertools import combinations

n, m = map(int, input().split())
is_possible = [[True for _ in range(n)] for _ in range(n)] # 가능한 조합인지 쉽게 파악할 수 있다.

for _ in range(m):
    a, b = map(int, input().split())
    is_possible[a-1][b-1] = False
    is_possible[b-1][a-1] = False

re = 0
for comb in combinations(range(n), 3):
    a, b, c = comb
    if is_possible[a][b] and is_possible[b][c] and is_possible[c][a]:
        re += 1

print(re)