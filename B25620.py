# python3는 시간초과
# pypy3로 해야 정답

import sys
import heapq
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

heap = list()
num_zeros = 0
for i in range(N):
    if A[i] == 0:
        num_zeros += 1
    else :
        heapq.heappush(heap, A[i])

for _ in range(Q):
    x, y = map(int, input().split())
    if y == 1:
        continue
    tmp = []
    while len(heap) != 0:
        v = heap[0] # heap에서 가장 작은 값
        if v > x: # 가장 작은 값이 x보다 큰 경우 굳이 진행할 필요 없음
            break

        heapq.heappop(heap) # 최소값 추출
        v *= y # y만큼 곱해준다.
        if v == 0: # 곱해서 0이 되는 경우
            num_zeros += 1 # 0 개수 1 증가
        else : # tmp에 v값 추가
            tmp.append(v)
    # 새롭게 연산된 값 heap에 추가
    for t in tmp:
        heapq.heappush(heap, t)

for i in range(num_zeros):
    print(0, end=' ')

while len(heap) != 0:
    v = heapq.heappop(heap)
    print(v, end=' ')