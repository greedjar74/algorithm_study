dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def DFS(current, dist):
    global cnt
    r = current[0]
    c = current[1]
    if r == 0 and c == C-1:
        if dist == K:
            cnt += 1
    else :
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != 'T' and not visited[nr][nc]:
                visited[nr][nc] = True
                DFS((nr, nc), dist+1)
                visited[nr][nc] = False

R, C, K = map(int, input().split())
board = [list(input()) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
visited[R-1][0] = True

cnt = 0
DFS((R-1, 0), 1)
print(cnt)