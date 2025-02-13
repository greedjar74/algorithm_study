from queue import PriorityQueue

n = int(input())
tmp_list = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
pair_list = []

for i in range(n):
    a, b = tmp_list[i][0], tmp_list[i][1]
    if abs(a - b) <= m:
        pair_list.append((min(a, b), max(a, b)))

pair_list.sort()
pq = PriorityQueue()
n = len(pair_list)

for i in range(n):
    pq.put(pair_list[i][1])

re = 0
for i in range(n):
    end = pair_list[i][0] + m
    while pq.qsize() != 0:
        x = pq.get()
        if end < x:
            pq.put(x)
            break
    
    re = max(re, n - i - pq.qsize())

print(re)