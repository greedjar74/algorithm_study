# DFS로 구현
# 실행시간이 BFS에 비해 획기적으로 줄어들었다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def DFS(nodes):
    global is_Tree
    c_node, p_node = nodes
    visited[c_node] = True
    for node in graph[c_node]:
        if p_node != None and node != p_node and visited[node]:
            is_Tree = False
        if not visited[node]:
            DFS((node, c_node))

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
            is_Tree = True
            DFS((i, None))
            if is_Tree:
                cnt += 1

    if cnt == 0:
        print(f"Case {c}: No trees.")
    elif cnt == 1:
        print(f"Case {c}: There is one tree.")
    else :
        print(f"Case {c}: A forest of {cnt} trees.")