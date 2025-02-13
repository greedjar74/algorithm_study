import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def BFS(start):
    need_visit = deque()
    need_visit.append(start)
    is_cycle = False

    while need_visit:
        current = need_visit.popleft()
        if visited[current]:
            is_cycle = True
        
        visited[current] = True
        
        for node in graph[current]:
            if not visited[node]:
                need_visit.append(node)
        
    return is_cycle

case = 0
while True:
    case += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    visited = [False for _ in range(n)]
    cnt = 0
    for i in range(n):
        if not visited[i]:
            is_cycle = BFS(i)
            if not is_cycle:
                cnt += 1
    
    if cnt > 1:
        print(f"Case {case}: A forest of {cnt} trees.")
    elif cnt == 1:
        print(f"Case {case}: There is one tree.")
    else :
        print(f"Case {case}: No trees.")