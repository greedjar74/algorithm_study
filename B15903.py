import heapq

n, m = map(int, input().split())
nums = list(map(int, input().split()))
heapq.heapify(nums)

for _ in range(m):
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    heapq.heappush(nums, a+b)
    heapq.heappush(nums, a+b)

print(sum(nums))