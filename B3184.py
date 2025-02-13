import sys
sys.setrecursionlimit(123458) # recursion 오류를 방지하기 위함

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def DFS(current):
    if graph[current[0]][current[1]] == 'v':
        tmp[1] += 1
    elif graph[current[0]][current[1]] == 'o':
        tmp[0] += 1
    for i in range(4):
        nr = current[0] + dr[i]
        nc = current[1] + dc[i]
        if (0 <= nr < R) and (0 <= nc < C) and (not visited[nr][nc]) and graph[nr][nc] != '#':
            visited[nr][nc] = True
            DFS((nr, nc))

R, C = map(int, input().split())
graph = list(list(input()) for _ in range(R))
visited = [[False for _ in range(C)] for _ in range(R)]
o_cnt = 0
v_cnt = 0

for i in range(R):
    for j in range(C):
        if (not visited[i][j]) and (graph[i][j] != '#'):
            visited[i][j] = True
            tmp = [0, 0]
            DFS((i, j))
            if tmp[0] > tmp[1]:
                o_cnt += tmp[0]
            else :
                v_cnt += tmp[1]

print(o_cnt, v_cnt)