# python3 시간초과 발생
# pypy3 가능

import sys
from collections import deque
input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def BFS(start, h):
    need_visit = deque()
    need_visit.append(start)
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[start[0]][start[1]] = True

    while need_visit:
        r, c = need_visit.popleft()
        if r == 0 or r == n-1 or c == 0 or c == m-1:
            return False
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and board[nr][nc] <= h and not visited[nr][nc]:
                need_visit.append((nr, nc))
                visited[nr][nc] = True

    return True

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]

re = 0
for r in range(n):
    for c in range(m):
        while BFS((r, c), board[r][c]):
            board[r][c] += 1
            re += 1

print(re)