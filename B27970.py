S = list(input())
mod = int(1e9 + 7)

re = 0
power = 1
for i in range(len(S)):
    if S[i] == 'O':
        re += power
        re %= mod
    power *= 2
    power %= mod

print(re)