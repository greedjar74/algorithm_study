'''
점화식
1. 현재 노드를 선택한다. -> 바로 다음 자식 노드는 선택할 수 없다. -> D[current] = weights[current] + E[next]
2. 현재 노드를 선택하지 않는다.
    2-1. 바로 다음 자식 노드 선택한다. -> E[current] = D[next]
    2-2. 바로 다음 자식 노드를 선택하지 않는다. E[current] = E[next]
'''

def DFS(current):
    visited[current] = True
    
    D[current] = weights[current]
    D_route[current].append(current)
    E[current] = 0

    for node in graph[current]:
        if not visited[node]:
            DFS(node)
            D[current] += E[node]
            D_route[current].extend(E_route[node])

            if D[node] < E[node]:
                E[current] += E[node]
                E_route[current].extend(E_route[node])
            else :
                E[current] += D[node]
                E_route[current].extend(D_route[node])

n = int(input())
weights = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

visited = [False for _ in range(n)]

D = [0 for _ in range(n)] # 현재 노드를 선택하는 경우
D_route = [[] for _ in range(n)]

E = [0 for _ in range(n)] # 현재 노드를 선택하지 않는 경우
E_route = [[] for _ in range(n)]

DFS(0)

if D[0] < E[0]:
    print(E[0])
    E_route[0].sort()
    print(*list(map(lambda x: x + 1, E_route[0])))

else :
    print(D[0])
    D_route[0].sort()
    print(*list(map(lambda x: x + 1, D_route[0])))