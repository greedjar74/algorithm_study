import sys
from queue import PriorityQueue

input = sys.stdin.readline

N, M = map(int, input().split())
stats = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    tmp.sort()
    stats.append(tmp)

pq = PriorityQueue()
mx = 0 # 최대값 -> 능력치의 '최대-최소'를 구하기 위해 찾아둔다.
for i in range(N):
    pq.put((stats[i][0], i)) # 해당 능력치가 몇 반에서 나왔는지 같이 저장한다.
    mx = max(mx, stats[i][0])

idx_list = [0 for _ in range(N)]

re = sys.maxsize
while True:
    mn, id = pq.get() # 최소값 추출
    re = min(re, mx - mn) # 새롭게 찾은 최대-최소 차이와 기존 결과 중 더 작은 값 채택
    idx_list[id] += 1 # 최소값인 반에서 다음 능력치로 이동
    
    if idx_list[id] >= M: # M보다 같거나 커지는 경우 -> 더이상 최소값은 변하지 않는다.
        break

    pq.put((stats[id][idx_list[id]], id))
    mx = max(mx, stats[id][idx_list[id]]) # 최대값 업데이트

print(re)