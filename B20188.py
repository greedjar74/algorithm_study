# 실패

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def preorder(current):
    if len(graph[current]) == 1:
        path.append(current)
        return

    for node in graph[current]:
        if not visited[node]:
            visited[node] = True
            dist[node] = dist[current] + 1
            preorder(node)
            if not in_path[current]:
                in_path[current] = True
                path.append(current)

N = int(input().strip())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(N+1)]
in_path = [False for _ in range(N+1)]
dist = [0 for _ in range(N+1)]
path = []
visited[1] = True
preorder(1)
print(path)
print(dist)