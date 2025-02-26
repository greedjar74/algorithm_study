# 시간초과 발생

import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
graph = [[INF for _ in range(N)] for _ in range(N)]
for i in range(N):
    graph[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c

s, t = map(int, input().split())
s -= 1
t -= 1

dist = graph[s][:]
need_visit = deque()
for i in range(N):
    if i != s and dist[i] < INF:
        need_visit.append(i)

visited = [False for _ in range(N)]
visited[s] = True

while need_visit:
    current = need_visit.popleft()
    visited[current] = True
    for i in range(N):
        if dist[current] + graph[current][i] < dist[i]:
            dist[i] = dist[current] + graph[current][i]
        if not visited[i] and graph[current][i] != INF:
            need_visit.append(i)

print(dist[t])