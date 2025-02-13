# DFS로 하면 시간초과 발생

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def DFS(r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and not alpha_check[board[nr][nc]]:
            visited[nr][nc] = True
            alpha_check[board[nr][nc]] = True
            tmp[nr][nc] = tmp[r][c] + 1
            re[nr][nc] = max(re[nr][nc], tmp[nr][nc])
            DFS(nr, nc)
            visited[nr][nc] = False
            alpha_check[board[nr][nc]] = False
            tmp[nr][nc] -= 1

R, C = map(int, input().split())
board = list(list(input()) for _ in range(R))

alpha_check = {'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False, 'G': False, 'H': False, 'I': False,
               'J': False, 'K': False, 'L': False, 'M': False, 'N': False, 'O': False, 'P': False, 'Q': False, 'R': False,
               'S': False, 'T': False, 'U': False, 'V': False, 'W': False, 'X': False, 'Y': False, 'Z': False}
alpha_check[board[0][0]] = True

visited = [[False for _ in range(C)] for _ in range(R)]
visited[0][0] = True

re = [[-1 for _ in range(C)] for _ in range(R)]
re[0][0] = 1

tmp = [[0 for _ in range(C)] for _ in range(R)]
tmp[0][0] = 1

DFS(0, 0)
mx = -1
for i in range(R):
    for j in range(C):
        mx = max(re[i][j], mx)

print(mx)