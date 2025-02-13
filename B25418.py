from collections import deque

def calcul(num, i):
    if i == 0:
        return num + 1
    else :
        return num * 2

def BFS():
    visited = {a:0}
    need_visit = deque()
    need_visit.append(a)

    while need_visit:
        current = need_visit.popleft()
        for i in range(2):
            next = calcul(current, i)
            
            if next == k:
                return visited[current] + 1
            
            elif next not in visited and next < k:
                visited[next] = visited[current] + 1
                need_visit.append(next)

a, k = map(int, input().split())
print(BFS())