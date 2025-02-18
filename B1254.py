import sys
input = sys.stdin.readline

def sol(num):
    if num <= 0:
        return 1
    try :
        return visited[num]
    except :
        tmp1 = num//P - X
        tmp2 = num//Q - Y
        visited[num] = sol(tmp1) + sol(tmp2)
        return visited[num]
    
# sol보다 수행 시간이 짧다.
def sol2(num):
    if num <= 0: 
        return 1
    elif num in visited:
        return visited[num]
    
    tmp1 = num//P - X
    tmp2 = num//Q - Y
    visited[num] = sol(tmp1) + sol(tmp2)
    return visited[num]

N, P, Q, X, Y = map(int, input().split())
visited = dict()
print(sol(N))