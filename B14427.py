import sys
from queue import PriorityQueue
input = sys.stdin.readline

N = int(input().strip())
nums = list(map(int, input().split()))
M = int(input().strip())

pq = PriorityQueue()
for i in range(N):
    pq.put((nums[i], i))

for _ in range(M):
    query = list(map(int, input().split()))
    if query[0] == 1:
        nums[query[1]-1] = query[2]
        pq.put((query[2], query[1]-1))
    else :
        while True:
            num, idx = pq.get()
            if nums[idx] == num:
                print(idx+1)
                pq.put((num, idx))
                break