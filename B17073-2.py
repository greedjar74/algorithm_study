import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(current):
    for node in graph[current]:
        if not visited[node]:
            real_graph[current].append(node)
            visited[node] = True
            DFS(node)

N, W = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

real_graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
visited[1] = True
DFS(1)

cnt = 0 
for i in range(1, N+1):
    if len(real_graph[i]) == 0:
        cnt += 1

print(W/cnt)