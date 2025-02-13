import sys

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def DFS():
    global mn

    if len(centers) == 3:
        s = 0

        for c in centers:
            s += board[c[0]][c[1]]
            for i in range(4):
                s += board[c[0] + dr[i]][c[1] + dc[i]]

        mn = min(mn, s)

    else :
        for r in range(1, n-1):
            for c in range(1, n-1):
                if not visited[r][c]:
                    p = 0
                    for i in range(4):
                        if not visited[r+dr[i]][c+dc[i]]:
                            p += 1

                    if p == 4:
                        centers.append((r, c))
                        visited[r][c] = True
                        for i in range(4):
                            visited[r+dr[i]][c+dc[i]] = True
                        DFS()

                        centers.pop()
                        visited[r][c] = False
                        for i in range(4):
                            visited[r+dr[i]][c+dc[i]] = False

n = int(input())
board = list(list(map(int, input().split())) for _ in range(n))
centers = []
mn = sys.maxsize
visited = [[False for _ in range(n)] for _ in range(n)]
DFS()
print(mn)