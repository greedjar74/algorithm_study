import sys
from itertools import product
input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def DFS(path, current):
    if len(path) == 4:
        routes.append(path[:])
    
    else :
        for i in range(4):
            nr = current[0] + dr[i]
            nc = current[1] + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                path.append((nr, nc))
                visited[nr][nc] = True
                DFS(path, (nr, nc))
                path.pop()
                visited[nr][nc] = False

def get_total(routes):
    re = 0
    point_visited = [[False for _ in range(N)] for _ in range(N)]
    for route in routes:
        for r, c in route:
            if point_visited[r][c]:
                return 0
            
            point_visited[r][c] = True
            re += board[r][c]
    
    return re

N, M = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(N))
start_points = []
for _ in range(M):
    a, b = map(int, input().split())
    start_points.append((a-1, b-1))

freinds_routes = []
for i in range(M):
    routes = []
    visited = [[False for _ in range(N)] for _ in range(N)]
    DFS([start_points[i]], (start_points[i][0], start_points[i][1]))
    freinds_routes.append(routes)

re = 0
for comb in product(*freinds_routes):
    re = max(re, get_total(comb))

print(re)