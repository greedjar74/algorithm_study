# 47점

import sys
input = sys.stdin.readline

def DFS(current, parent):
    global re

    for node in graph[current]:
        if node != parent:
            DFS(node, current)
            dp[current] += dp[node] + 1
    
    val = (dp[current] + 1)*(N-dp[current]-1) + (dp[current]*(dp[current]+1)//2)

    if current != 1:
        re += val

N = int(input().strip())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [0 for _ in range(N+1)]
re = 0
DFS(1, 0)

print(re)