# dp를 활용해서 풀이

n = int(input())
homework = list()
limit = 0
for _ in range(n):
    time, score = map(int, input().split())
    homework.append((time, score))
    if limit < time:
        limit = time

homework.sort(key= lambda x: (x[0], -x[1]))
dp = [[0 for _ in range(limit + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, limit + 1):
        time, score = homework[i-1]
        if time >= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + score)
        else :
            dp[i][j] = dp[i][j-1]

print(dp[-1][-1])