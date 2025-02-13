import sys
input = sys.stdin.readline

N = int(input())
S = list(input().strip() for _ in range(N))
S = list(set(S))
n = len(S)
cnt = n

for i in range(n):
    for j in range(n):
        if i != j and len(S[i]) <= len(S[j]) and S[i] == S[j][:len(S[i])]:
            cnt -= 1
            break

print(cnt)