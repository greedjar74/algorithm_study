import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
in_cnt = [0 for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    in_cnt[b-1] += 1
    graph[a-1].append(b-1)

re = [1 for _ in range(N)]
need_visit = deque()
for i in range(N):
    if in_cnt[i] == 0:
        need_visit.append(i)

while need_visit:
    current = need_visit.popleft()
    for node in graph[current]:
        in_cnt[node] -= 1
        if in_cnt[node] == 0:
            re[node] = re[current] + 1
            need_visit.append(node)

print(*re)