import heapq

a = []
b = []
for i in range(10, -1, -1):
    heapq.heappush(a, -i)
    b.append(-i)

print(a)
print(b)
for _ in range(10):
    print(heapq.heappop(a))