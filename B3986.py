n = int(input())
re = 0

for _ in range(n):
    word = input()
    tmp = []
    for i in range(len(word)):
        if len(tmp) > 0 and tmp[-1] == word[i]:
            tmp.pop(-1)
        else :
            tmp.append(word[i])

    if len(tmp) == 0:
        re += 1

print(re)