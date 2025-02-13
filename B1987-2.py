# visited를 따로 체크하지 않는다. -> 알파벳을 체크하면 이전 노드의 값이 체크되므로 이동하지 못한다!!

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
answer = 0

def DFS(r, c, cnt):
    global answer
    answer = max(answer, cnt)

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < R and 0 <= nc < C and not alpha_check[board[nr][nc]]:
            alpha_check[board[nr][nc]] = True
            DFS(nr, nc, cnt + 1)
            alpha_check[board[nr][nc]] = False

R, C = map(int, input().split())
board = list(list(input()) for _ in range(R))

alpha_check = {'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False, 'G': False, 'H': False, 'I': False,
               'J': False, 'K': False, 'L': False, 'M': False, 'N': False, 'O': False, 'P': False, 'Q': False, 'R': False,
               'S': False, 'T': False, 'U': False, 'V': False, 'W': False, 'X': False, 'Y': False, 'Z': False}
alpha_check[board[0][0]] = True

DFS(0, 0, 1)
print(answer)