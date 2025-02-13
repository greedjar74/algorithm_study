# DFS로 거리 구하기 -> BFS에 비해 훨씬 빠르게 수해된다.

from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def DFS(current):
    for node in graph[current]:
        if leaf[node] and dist[node] == 0:
            dist[node] = dist[current] + 1
            DFS(node)


N = int(input().strip())
graph = [[] for _ in range(N+1)]
degrees = [0 for _ in range(N+1)]
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    degrees[a] += 1
    degrees[b] += 1

need_visit = deque()
leaf = [False for _ in range(N+1)]
for i in range(N+1):
    if degrees[i] == 1:
        need_visit.append(i)
        degrees[i] = -1
        leaf[i] = True

while need_visit:
    current = need_visit.popleft()
    for node in graph[current]:
        degrees[node] -= 1
        if degrees[node] == 1:
            need_visit.append(node)
            leaf[node] = True

dist = [0 for _ in range(N+1)]
for i in range(1, N+1):
    if not leaf[i]:
        DFS(i)

print(*dist[1:])