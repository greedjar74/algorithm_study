def find_start():
    for i in range(n):
        for j in range(m):
            if board[i][j] == '#':
                return (i, j)
            
n, m = map(int, input().split())
board = list(list(input()) for _ in range(n))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
r, c = find_start()
d = 0

while True:
    tmp = 0
    for i in range(4):
        if 0 <= r+dr[i] < n and 0 <= c+dc[i] < m and board[r+dr[i]][c+dc[i]] == '#':
            tmp += 1

    if tmp < 2:
        break

    if r+dr[d] >= n or r+dr[d] < 0 or c+dc[d] >= m or c+dc[d] < 0 or board[r+dr[d]][c+dc[d]] == '.':
        d = (d+1) % 4
    
    r, c = r+dr[d], c+dc[d]
    

directions = ['UP', 'RIGHT', 'DOWN', 'LEFT']
print(directions[d])