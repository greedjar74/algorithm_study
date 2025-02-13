# 남우, 유령에 대해서 각각 BFS 수행 -> 시간초과 발생

import sys
from collections import deque

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def BFS(start, mode):
    need_visit = deque()
    need_visit.append(start)
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visited[start[0]][start[1]] = 0

    while need_visit:
        current = need_visit.popleft()
        for i in range(4):
            nr = current[0] + dr[i]
            nc = current[1] + dc[i]
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == -1:
                if mode == 0:
                    if board[nr][nc] != '#':
                        visited[nr][nc] = visited[current[0]][current[1]] + 1
                        need_visit.append((nr, nc))
                
                else :
                    visited[nr][nc] = visited[current[0]][current[1]] + 1
                    need_visit.append((nr, nc))

    return visited[end_point[0]][end_point[1]]

n, m = map(int, input().split())
board = list(list(input()) for _ in range(n))
g_starts = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 'G':
            g_starts.append((i, j))
        elif board[i][j] == 'N':
            n_start = (i, j)
        elif board[i][j] == 'D':
            end_point = (i, j)

n_end_time = BFS(n_start, 0)

g_end_time = sys.maxsize
for g_start in g_starts:
    g_end_time = min(g_end_time, BFS(g_start, 1))

if n_end_time == -1 or (n_end_time != -1 and n_end_time >= g_end_time):
    print('No')
else :
    print('Yes')