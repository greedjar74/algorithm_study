import sys
input = sys.stdin.readline

def DFS(current):
    is_leaf = True
    for node, w in graph[current]:
        if not visited[node]:
            visited[node] = True
            DFS(node)
            dp[current] += min(dp[node], w)
            is_leaf = False
        
    if current != 1 and is_leaf:
        dp[current] = sys.maxsize

T = int(input().strip())
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))

    visited = [False for _ in range(N+1)]
    dp = [0 for _ in range(N+1)]
    visited[1] = True

    DFS(1)
    print(dp[1])