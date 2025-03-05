import sys
import heapq
input = sys.stdin.readline

def BFS():
    visited = [False for _ in range(N+1)]
    need_visit = list()
    heapq.heappush(need_visit, (-1*A[1], 1))
    cnt = 0

    while need_visit:
        a, current = heapq.heappop(need_visit)
        cnt += a * -1
        print(cnt)
        for node in graph[current]:
            if not visited[node]:
                visited[node] = True
                heapq.heappush(need_visit, (-1*A[node], node))

N = int(input().strip())
P = list(map(int, input().split()))
A = list(map(int, input().split()))
A.insert(0, 0)

graph = [[] for _ in range(N+1)]
for i in range(len(P)):
    graph[P[i]].append(i+2)

BFS()