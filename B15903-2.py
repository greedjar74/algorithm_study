from queue import PriorityQueue

n, m = map(int, input().split())
nums = list(map(int, input().split()))
pq = PriorityQueue()

for i in range(n):
    pq.put(nums[i])

for _ in range(m):
    a = pq.get()
    b = pq.get()
    pq.put(a + b)
    pq.put(a + b)

re = 0
for _ in range(n):
    re += pq.get()
print(re)