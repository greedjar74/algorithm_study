from collections import deque
import sys

input = sys.stdin.readline

def BFS(start):
    need_visit = deque()
    need_visit.append(start)
    visited = [False for _ in range(n)]
    visited[start] = True

    while need_visit:
        current = need_visit.popleft()
        for node in graph[current]:
            if not visited[node]:
                visited[node] = True
                need_visit.append(node)

    return visited

n, k = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(k):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)

possible = []
for i in range(n):
    tmp = BFS(i)
    possible.append(tmp[:])

s = int(input().strip())
for _ in range(s):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    if possible[u][v]:
        print(-1)
    elif possible[v][u]:
        print(1)
    else :
        print(0)