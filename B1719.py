import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]
re = [['-' for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
    re[a][b] = b
    re[b][a] = a

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                continue
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                re[i][j] = re[i][k]

for line in re[1:]:
    print(*line[1:], sep=' ')