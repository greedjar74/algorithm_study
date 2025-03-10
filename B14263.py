import sys
from queue import PriorityQueue
input = sys.stdin.readline

N, M = map(int, input().split())
B = list(list(input()) for _ in range(N))

graph = dict() # 위상정렬 그래프
cnt = dict() # 각 카드가 놓이기 전 필요한 카드의 개수 -> 0이 되면 놓을 수 있는 카드
check = set() # 특정 카드를 체크했는지 확인
possible = True # 가능한 경우인지 확인

# 그리드의 모든 영역에 대해서 수행
for i in range(N):
    for j in range(M):
        # .이 아니며 이전에 체크한적 없는 카드에 대해서만 수행
        if B[i][j] == '.' or B[i][j] in check:
            continue
        cc = B[i][j] # 현재 카드 값
        check.add(cc) # 현재 카드를 체크했다고 저장
        graph[cc] = [] # 위상정렬 그래프에 노드 생성
        # cnt에 없다면 key값을 만들어준다.
        if cc not in cnt:
            cnt[cc] = 0 # 들어오는 간선의 개수를 0으로 초기화

        # 현재 카드값을 가지는 위치의 row, column값들을 저장
        rs, cs = list(), list()
        for r in range(N):
            for c in range(M):
                if B[r][c] == cc:
                    rs.append(r)
                    cs.append(c)
        # 현재 카드의 영역을 찾는다. -> (min_r, min_c), (max_r, max_c)를 구하면 영역을 알 수 있다.
        min_r, max_r, min_c, max_c = min(rs), max(rs), min(cs), max(cs)

        # 현재 카드 영역 내부에 다른 카드가 있는지 확인
        for r in range(min_r, max_r+1):
            if not possible: # 불가능한 경우 종료
                break
            for c in range(min_c, max_c+1):
                if B[r][c] != cc: # 다른 카드가 있는 경우
                    if B[r][c] == '.': # .이 존재하는 경우 불가능 -> .은 카드가 아닌 빈공간을 의미
                        possible = False # 불가능
                        break
                    graph[cc].append(B[r][c]) # 현재 카드에서 이동할 수 있는 노드 추가 -> 현재 카드 이후에 놓인다는 의미
                    if B[r][c] not in cnt:
                        cnt[B[r][c]] = 0
                    cnt[B[r][c]] += 1 # 다음으로 놓이는 카드에 들어가는 간선 1증가

if not possible:
    print(-1)
else :
    pq = PriorityQueue() # 현재 놓일 수 있는 카드들 중 값이 가장 작은 값을 뽑기 위해 PriorityQueue 활용
    for k, v in cnt.items():
        if v == 0: # 들어오는 간선이 0인 카드
            pq.put(k) # pq에 추가
    re = [] # 순서를 저장하는 결과 변수
    while pq.qsize() != 0: # 놓을 수 있는 카드가 존재하는 경우
        u = pq.get() # 가장 값이 작은 카드 추출
        re.append(u) # 결과에 저장
        for v in graph[u]: # 현재 놓인 카드와 연결된 카드의 들어오는 간선 수 1 감소
            cnt[v] -= 1
            if cnt[v] == 0: # 들어오는 간선이 0이 된 경우
                pq.put(v) # pq에 추가

    if len(re) != len(graph): # 결과 값의 길이가 카드의 개수와 일치하지 않는 경우 -> 불가능한 경우 -> 싸이클 발생
        print(-1)
    else :
        print("".join(re))