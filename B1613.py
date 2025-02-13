# 시간초과 발생

import sys

N, K = map(int, input().split())
graph = [[sys.maxsize for _ in range(N)] for _ in range(N)]
for i in range(N):
    graph[i][i] = 0

for _ in range(K):
    u, v = map(int, input().split())
    graph[u-1][v-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
    
m = int(input())
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if graph[u][v] < sys.maxsize:
        print(-1)
    elif graph[v][u] < sys.maxsize:
        print(1)
    else :
        print(0)