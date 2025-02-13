import sys
from queue import PriorityQueue
input = sys.stdin.readline

N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]

for _ in range(N):
    a, b, c = map(int, input().split())
    if b <= D:
        graph[a].append((b, c))

for i in range(D):
    graph[i].append((i+1, 1))

dist = [sys.maxsize for _ in range(D+1)]
pq = PriorityQueue()
pq.put((0, 0))
dist[0] = 0

while pq.qsize() != 0:
    u, d = pq.get() # 매번 (u, d)값이 작은 데이터 부터 추출한다.
    
    # u노드에 대해 가장 최신에 갱신된 값만 사용
    # d는 u노드로 가는데 필요한 거리를 의미한다.
    # 만약 d가 10인데 dist[u]가 새롭게 갱신되어 3이 되었다면 해당 값은 사용하지 않는다.
    # 이게 핵심이다.
    if d != dist[u]:
        continue

    for v, w in graph[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            pq.put((v, dist[v]))

print(dist[D])