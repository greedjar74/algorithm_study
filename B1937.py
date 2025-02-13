import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def DFS(current):
    r, c = current
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if board[nr][nc] > board[r][c]:
                if visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    DFS((nr, nc))
                visited[r][c] = max(visited[r][c], visited[nr][nc] + 1)

N = int(input().strip())
board = list(list(map(int, input().split())) for _ in range(N))
visited = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            visited[i][j] = 1
            DFS((i, j))

mx = 0
for i in range(N):
    mx = max(max(visited[i]), mx)

print(mx)