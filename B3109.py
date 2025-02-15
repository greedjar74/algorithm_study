import sys
input = sys.stdin.readline

dr = [-1, 0, 1]
dc = [1, 1, 1]

def DFS(r, c):
    global re, comp
    for i in range(3):
        nr = r + dr[i]
        nc = c + dc[i]
        if not comp and 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and board[nr][nc] == '.':
            if nc == C-1:
                comp = True
                re += 1
            visited[nr][nc] = True
            DFS(nr, nc)


R, C = map(int, input().split())
board = list(list(input().strip()) for _ in range(R))

visited = [[False for _ in range(C)] for _ in range(R)]
re = 0
for i in range(R):
    visited[i][0] = True
    comp = False
    DFS(i, 0)

print(re)