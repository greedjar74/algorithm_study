from collections import deque
import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    graph = [[] for _ in range(N)]
    in_degree = [0 for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        in_degree[b-1] += 1
    
    starts = []
    for i in range(N):
        if in_degree[i] == 0:
            starts.append(i)

    visited = nums[:]
    for start in starts:
        need_visit = deque()
        need_visit.append(start)

        while need_visit:
            current = need_visit.popleft()
            for node in graph[current]:
                in_degree[node] -= 1
                if in_degree[node] ==0:
                    need_visit.append(node)

                visited[node] = max(visited[node], visited[current] + nums[node])

    W = int(input().strip())
    print(visited[W-1])