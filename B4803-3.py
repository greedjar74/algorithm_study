# BFS를 사용해서 싸이클 탐지

from collections import deque
import sys

input = sys.stdin.readline

def BFS(start):
    need_visit = deque()
    need_visit.append(start)
    is_Tree = True
    
    while need_visit:
        current = need_visit.popleft()
        if visited[current]:
            is_Tree = False # 이걸 return False로 하면 오답이 된다. 왜 그런거야...? -> return을 하면 연결된 모든 노드에 대해서 검사를 수행하지 못한다. 따라서 잘못된 결과가 만들어진다!!!!!
        visited[current] = True
        for node in graph[current]:
            if not visited[node]:
                need_visit.append(node)
    
    return is_Tree

c = 0
while True:
    c += 1
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    visited = [False for _ in range(N)]
    cnt = 0

    for i in range(N):
        if not visited[i]:
            if BFS(i):
                cnt += 1

    if cnt == 0:
        print(f"Case {c}: No trees.")
    elif cnt == 1:
        print(f"Case {c}: There is one tree.")
    else :
        print(f"Case {c}: A forest of {cnt} trees.")