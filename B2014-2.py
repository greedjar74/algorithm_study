# 우선순위 큐를 사용하여 수행시간 축소

import heapq

m, n = map(int, input().split())
nums = list(map(int, input().split()))
heap = []

for num in nums:
    heapq.heappush(heap, num)

for _ in range(n):
    v = heapq.heappop(heap)
    for num in nums:
        tmp = v * num
        if tmp >= 2 ** 31:
            break
        
        heapq.heappush(heap, tmp)

        if v % num == 0:
            break

print(v)