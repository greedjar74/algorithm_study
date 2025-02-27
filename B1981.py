import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
A = list(list(map(int, input().split())) for _ in range(N))

left = 0
right = 200
re = -1

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

while left <= right:
    mid = (left + right) // 2
    is_possible = False # mid값을 차이로 가지는 경우가 존재하는지 판단

    for mn in range(200 - mid + 1): # 차이가 mid인 경우 가능한 mn값들에 대해 모두 탐색 -> mx = mn + mid
        mx = mn + mid
        if mn <= A[0][0] <= mx and mn <= A[N-1][N-1] <= mx: # 시작, 끝 값이 해당 범위에 부합하지 않는 경우는 제외
            visited = [[False for _ in range(N)] for _ in range(N)]
            need_visit = deque()
            need_visit.append((0, 0))

            while need_visit:
                r, c = need_visit.popleft()
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < N and 0 <= nc < N and mn <= A[nr][nc] <= mx and not visited[nr][nc]:
                        visited[nr][nc] = True
                        need_visit.append((nr, nc))
            
            if visited[N-1][N-1]: # 끝 지점에 도달한 경우
                is_possible = True
                break

    if is_possible:
        re = mid
        right = mid-1 # 더 작은 값 탐색

    else :
        left = mid + 1 # 더 큰 값 탐색

print(re)