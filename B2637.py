# 위상정렬 사용!!
from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
in_cnt = [0 for _ in range(n+1)]
is_base = [0 for _ in range(n+1)]

for _ in range(m):
    x, y, k = map(int, input().split())
    graph[x].append((y, k))
    in_cnt[y] += 1
    is_base[x] += 1

dp = [0 for _ in range(n+1)]
dp[n] = 1
need_visit = deque()
need_visit.append(n)

while need_visit:
    current = need_visit.popleft()
    for next in graph[current]:
        dp[next[0]] += dp[current] * next[1]
        in_cnt[next[0]] -= 1
        if in_cnt[next[0]] == 0:
            need_visit.append(next[0])

for i in range(1, n):
    if is_base[i] == 0:
        print(i, dp[i])