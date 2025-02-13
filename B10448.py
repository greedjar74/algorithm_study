from itertools import combinations

T = int(input())

# n은 최대 45까지 가능
# 미리 T_i값을 구해둔다.
T_nums = [0 for _ in range(46)]
T_nums[0] = 1
for i in range(1, 46):
    T_nums[i] = T_nums[i-1] + i + 1

for _ in range(T):
    N = int(input())
    is_possible = False # 가능한지 체크

    # 1개의 숫자를 선택해서 더한다.
    if N % 3 == 0 and N // 3 in T_nums:
        print(1)
        continue

    # 3개의 숫자를 선택해서 더한다.
    for comb in combinations(T_nums, 3):
        if sum(comb) == N:
            is_possible = True
            break
    if is_possible:
        print(1)
        continue

    # 2개의 숫자를 선택해서 더한다.
    for comb in combinations(T_nums, 2):
        if comb[0] * 2 + comb[1] == N or comb[0] + comb[1] * 2 == N:
            is_possible = True
            break
    if is_possible:
        print(1)
        continue

    print(0)