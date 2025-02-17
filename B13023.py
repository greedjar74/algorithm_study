# 13023

import sys
input = sys.stdin.readline

def DFS(current, visited):
    tmp = visited[:]
    
    if len(tmp) == 5:
        print(1)
        exit(0)

    for nxt in graph[current]:
        if nxt not in tmp:
            DFS(nxt, tmp + [nxt])

n, m = map(int, input().split())
graph = dict()

for i in range(n):
    graph[i] = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    DFS(i, [i])

print(0)