import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

heap = []
for i in range(1, N-K):
    heapq.heappush(heap, (nums[i]-nums[i-1], i-1))

re = sys.maxsize
for i in range(0, K+1):
    M = nums[i+N-K-1] - nums[i]
    m, idx = heap[0]
    re = min(re, M+m)

    if i != K:
        heapq.heappush(heap, (nums[i+N-K]-nums[i+N-K-1], i+N-K-1))
        while len(heap) != 0:
            val, idx = heap[0]
            if idx <= i:
                heapq.heappop(heap)
                continue
            break

print(re)