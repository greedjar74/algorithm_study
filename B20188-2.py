import sys
input = sys.stdin.readline

def DFS(current):
    dp[current] = 1
    for node in graph[current]:
        if not visited[node]:
            visited[node] = True
            DFS(node)
            dp[current] += dp[node]

N = int(input().strip())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [0 for _ in range(N+1)]
visited = [False for _ in range(N+1)]
visited[1] = True

DFS(1)

re = 0 
for i in range(2, N+1):
    re += dp[i] * (dp[i]-1) // 2
    re += dp[i] * (N-dp[i])

print(re)