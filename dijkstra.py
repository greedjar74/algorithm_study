# 그래프가 주어질 때 특정 노드에서 다른 모든 노드로 가는 가장 짧은 거리를 구한다.
# 다익스트라 핵심 : 매번 가장 짧은 간선을 선택한다!
# 선택된 간선의 개수가 N-1이 되면 끝

# 아래 코드는 1에서 시작해서 다른 모든 노드로 가는 가장 짧은 거리를 구한다.

import sys

def dijkstra(W):
    n = len(W) - 1
    F = []
    touch = [-1 for _ in range(n+1)] # 특정 노드가 연결되었는지 여부 -> -1은 연결됨
    length = [-1 for _ in range(n+1)] # 1번 노드와의 거리
    for i in range(2, n+1):
        touch[i] = 1 # 시작 지점을 1으로 모두 초기화
        length[i] = W[1][i]

    for _ in range(n-1): # 간선의 개수가 n-1개가 되면 모든 노드와 연결된 것
        minValue = sys.maxsize # 가장 거리가 짧은 값을 찾는다.
        for i in range(2, n+1): # 2~n번 노드로 가는 거리 중 가장 짧은 거리를 찾는다.
            if (0 <= length[i] and length[i] < minValue):
                minValue = length[i]
                vnear = i
        
        edge = (touch[vnear], vnear, W[touch[vnear]][vnear])
        F.append(edge)

        for i in range(2, n+1): # 2~n번 노드로 가는 거리 업데이트
            if (length[i] > length[vnear] + W[vnear][i]): # 기존 값보다 더 작은 경우
                length[i] = length[vnear] + W[vnear][i]
                touch[i] = vnear
        length[vnear] = -1

    return F

# 연결된 간선들의 길이 합
def length(F):
    total =  0
    for e in F:
        total += e[2]
    return total

INF = sys.maxsize
W = [
    [-1, -1, -1, -1, -1, -1],
    [-1, 0, 8, 4, 6, 1],
    [-1, INF, 0, INF, INF, INF],
    [-1, INF, 2, 0, 5, INF],
    [-1, INF, 3, INF, 0, INF],
    [-1, INF, INF, INF, 1, 0]
]

F = dijkstra(W)
for i in range(len(F)):
    print(F[i])
print(length(F))