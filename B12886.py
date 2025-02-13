from collections import deque

def BFS():
    need_visit = deque()
    need_visit.append((min(A, B), max(A, B)))
    visited = [[False for _ in range(S)] for _ in range(S)]
    visited[min(A, B)][max(A, B)] = True

    while need_visit:
        a, b = need_visit.popleft()
        c = S - a - b
        tmp = [a, b, c]
        for i in range(3):
            x, y = tmp[i], tmp[(i + 1) % 3]
            if x != y:
                x, y = min(x, y), max(x, y)
                if not visited[x+x][y-x]:
                    visited[x+x][y-x] = True
                    need_visit.append((x+x, y-x))
    
    if visited[S//3][S//3]:
        print(1)
    else :
        print(0)


A, B, C = map(int, input().split())
S = A + B + C

if S % 3 != 0:
    print(0)
else :
    BFS()