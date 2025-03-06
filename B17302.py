import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = list(list(input().strip()) for _ in range(N))

re = [[2 for _ in range(M)] for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for r in range(N):
    for c in range(M):
        cnt = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                cnt += 1

        if cnt % 2 == 1 and board[r][c] == 'W':
            re[r][c] = 3
            
        elif cnt % 2 == 0 and board[r][c] == 'B':
            re[r][c] = 3

print(1)
for i in range(N):
    for j in range(M):
        print(re[i][j], end='')
    print()