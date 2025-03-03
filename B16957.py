import sys
input = sys.stdin.readline

dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

def DFS(r, c):
    global cnt
    for nr, nc in graph[(r, c)]:
        cnt += 1
        DFS(nr, nc)

R, C = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(R))

graph = {(r, c): [] for r in range(R) for c in range(C)}
valley = []

for r in range(R):
    for c in range(C):
        mn = board[r][c]
        nxt_loc = (-1, -1)
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and mn > board[nr][nc]:
                mn = board[nr][nc]
                nxt_loc = (nr, nc)

        if nxt_loc != (-1, -1):
            graph[nxt_loc].append((r, c))
        else :
            valley.append((r, c))

re = [[0 for _ in range(C)] for _ in range(R)]
for vr, vc in valley:
    cnt = 1
    DFS(vr, vc)
    re[vr][vc] = cnt

for line in re:
    print(*line)