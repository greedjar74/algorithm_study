from collections import deque

def BFS(start):
    need_visit = deque()
    need_visit.append((start, 0))
    visited = [False for _ in range(n)]
    visited[start] = True
    s = 0

    while need_visit:
        c_node, l = need_visit.popleft()
        for node in graph[c_node]:
            if (not visited[node]) and l+1 <= 2:
                visited[node] = True
                need_visit.append((node, l+1))
                s += 1

    return s

n = int(input())
graph = [[] for _ in range(n)]

for i in range(n):
    tmp = list(input())
    for j in range(n):
        if tmp[j] == 'Y':
            graph[i].append(j)

re = 0
for i in range(n):
    re = max(BFS(i), re)

print(re)