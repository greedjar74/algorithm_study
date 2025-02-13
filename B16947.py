from collections import deque

n = int(input())
graph = [[] for _ in range(n)]

for _ in range(n):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

degree = [len(graph[node]) for node in range(n)] # 특정 노드와 연결된 노드의 개수들

# 지선 노드 제거
# 매번 연결된 노드가 하나만 존재하는 노드들을 제거하면 최종적으로 순환선만 남는다.
while True:
    # leaf 노드 탐색
    leaf = []
    for i in range(n):
        if degree[i] == 1: # 연결된 노드가 한 개인 경우 leaf
            leaf.append(i)

    # leaf노드가 없는 경우 종료
    if len(leaf) == 0:
        break

    # leaf노드 제거 및 leaf 노드와 연결된 노드의 간선 개수 1 감소
    for u in leaf:
        degree[u] = -1
        for v in graph[u]:
            degree[v] -= 1

# BFS

visited = [False for _ in range(n)]
dist = [0 for _ in range(n)]
need_visit = deque()

for i in range(n):
    if degree[i] > -1:
        need_visit.append(i)
        visited[i] = True

while need_visit:
    node = need_visit.popleft()
    for next in graph[node]:
        if not visited[next]:
            need_visit.append(next)
            visited[next] = True
            dist[next] = dist[node] + 1

print(*dist)