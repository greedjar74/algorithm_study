import sys
sys.setrecursionlimit(123458)

def DFS(current):
    for node in graph[current]:
        if not visited[node]:
            visited[node] = True
            DFS(node)
            if dp[node] > 0:
                dp[current] += dp[node]

n = int(input())
dp = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for i in range(2, n+1):
    t, a, p = input().split()
    if t == 'W':
        dp[i] = int(a) * -1
    else :
        dp[i] = int(a)
    graph[int(p)].append(i)

visited = [False for _ in range(n+1)]
visited[1] = True

DFS(1)
print(dp[1])