# 다시풀기!!!!

import itertools
n = int(input())
tmp = list(map(int, input().split()))
w = [0 for _ in range(4)]
for i in range(len(tmp)):
    w[tmp[i]] += 1
    
answer = 1e9
seq = list(itertools.permutations([1, 2, 3], 3))

for i in range(len(seq)):
    ans12, ans13, ans2, ans3 = 0, 0, 0, 0
    for j in range(w[seq[i][0]]):
        if tmp[j] == seq[i][1]:
            ans12 += 1
        if tmp[j] == seq[i][2]:
            ans13 += 1
    for j in range(w[seq[i][0]], w[seq[i][0]]+w[seq[i][1]]):
        if tmp[j] == seq[i][2]:
            ans2 += 1
    for j in range(w[seq[i][0]]+w[seq[i][1]], n):
        if tmp[j] == seq[i][1]:
            ans3 += 1
    answer = min(answer, ans12+ans13+max(ans2, ans3))
print(answer)