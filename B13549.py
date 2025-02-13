from collections import deque
import sys

def BFS(start, end):
    need_visit = deque()
    need_visit.append(start)
    visited = [-1 for _ in range(100001)]
    visited[start] = 0

    while need_visit:
        current = need_visit.popleft()

        if current == end:
            print(visited[current])
            return
        
        nx1 = current + 1
        nx2 = current - 1
        nx3 = current * 2

        if 0 <= nx1 <= 100000:
            if visited[nx1] > visited[current] + 1 or visited[nx1] == -1:
                visited[nx1] = visited[current] + 1
                need_visit.append(nx1)

        if 0 <= nx3 <= 100000:
            if visited[nx3] > visited[current] or visited[nx3] == -1:
                visited[nx3] = visited[current]
                need_visit.append(nx3)

        if 0 <= nx2 <= 100000:
            if visited[nx2] > visited[current] + 1 or visited[nx2] == -1:
                visited[nx2] = visited[current] + 1
                need_visit.append(nx2)

n, k = map(int, input().split())
BFS(n, k)