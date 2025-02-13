import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# start 노드부터 시작하여 BFS를 끝까지 돌고
# 사이클 존재 여부를 리턴하는 함수
def findCycle(start):
    isCycle = False
    q = deque()
    q.append(start)
    
    while q:
        cnt_node = q.popleft()
        # 노드를 큐에서 뽑았을 때 visited를 갱신해줌.
        # 이 때, 뽑은 노드의 visited가 이미 1인 경우는
        # 사이클이 존재한다는 것을 의미함
        # 예를 들어, 1-2, 2-3, 3-1인 사이클이 있다고 생각해보자.
        # 1에서 2와 3을 큐에 넣고 1의 visited는 1이 된다.
        # 그 다음 2를 큐에서 뽑고, visited를 1로 한 다음
        # 3을 큐에 넣는다(아직 1에서 넣은 3이 뽑기 전이므로 visited가 0)
        # 그 다음 1에서 넣은 3을 큐에서 뽑고 visited에 1을 넣는다.
        # 이제 큐에는 2에서 넣은 3이 아직 남아있다. 이 것을 뽑았을 때
        # visited[3]이 이미 1이므로 사이클로 판정

        if visited[cnt_node]:
            isCycle = True # 현재 뽑은 노드가 방문한적 있는 경우 싸이클 !!!!
        
        visited[cnt_node] = 1
        
        for adj_node in graph[cnt_node]:
            if visited[adj_node] == 0:
                q.append(adj_node)
                
    return isCycle

n, m = map(int, input().split())
case = 1

while n != 0 or m != 0:
    graph = [[] for _ in range(n+1)]
    visited = [0]*(n+1)
    count = 0
    
    # 양방향 매핑
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    # visited가 0인 모든 노드를 돌면서
    # 가능한 모든 연결 요소(연결 그래프)를 순회함
    for node in range(1, n+1):
        if visited[node] == 0:
            if not findCycle(node):
                count += 1
    
    if count == 0:
        print(f'Case {case}: No trees.')
    elif count == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {count} trees.')
    
    case += 1
    n, m = map(int, input().split())