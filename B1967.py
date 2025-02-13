# 또 풀이보고 풀었다...
# 풀이 핵심 : 초기 1번 노드에서 가장 먼 노드를 찾은 후 해당 노드에서 DFS를 다시 수행한다.
# pypy3로 제출하면 메모리 초과 발생

import sys
sys.setrecursionlimit(10**9)

def DFS(current):
    for node, w in graph[current]:
        if visited[node] == -1:
            visited[node] = visited[current] + w
            DFS(node)

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

visited = [-1 for _ in range(n+1)]
visited[1] = 0
DFS(1)

mx_depth_node = visited.index(max(visited))
visited = [-1 for _ in range(n+1)]
visited[mx_depth_node] = 0
DFS(mx_depth_node)

print(max(visited))