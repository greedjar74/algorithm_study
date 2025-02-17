from collections import deque
import sys
input = sys.stdin.readline

def BFS():
    visited = set()
    need_visit = deque()
    need_visit.append(S)
    visited.add(S)

    while need_visit:
        current = need_visit.popleft()

        if current * current <= 1e9 and current * current not in visited:
            need_visit.append(current * current)
            visited.add(current * current)
            path[current * current] = path[current] + "*"

        if current + current <= 1e9 and current + current not in visited:
            need_visit.append(current + current)
            visited.add(current + current)
            path[current + current] = path[current] + "+"
        
        if current / current <= 1e9 and current / current not in visited:
            need_visit.append(current / current)
            visited.add(current / current)
            path[current / current] = path[current] + "/"
        
        '''
        # -연산은 수행하는 순간 0이 되어 더이상 연산이 불가능하기에 굳이 만들지 않아도 된다.
        if current - current <= 1e9 and current - current not in visited:
            need_visit.append(current - current)
            visited.add(current - current)
            path[current - current] = path[current] + "-"
        '''
        
S, T = map(int, input().split())
path = {}
path[S] = ""
BFS()

if S == T:
    print(0)
elif T in path:
    print(path[T])
else :
    print(-1)