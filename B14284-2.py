import sys
from queue import PriorityQueue
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1

    graph[a].append((b, c))
    graph[b].append((a, c))

S, T = map(int, input().split())
S, T = S-1, T-1

dist = [sys.maxsize for _ in range(N)]
pq = PriorityQueue()
pq.put((0, S))
dist[S] = 0

while pq.qsize() != 0:
    d, u = pq.get() # 거리가 가장 짧은 간선을 추출
    if d != dist[u]: # 갱신된 거리값과 추출된 값이 다른 경우 -> 더 짧은 거리가 있으므로 사용하지 않는다.
        continue

    for v, w in graph[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            pq.put((dist[v], v))

print(dist[T])