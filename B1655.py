import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())
left_pq = []
right_pq = []

for i in range(N):
    num = int(input().strip())
    if i == 0:
        tmp = num
        print(num)
    elif i == 1:
        print(min(tmp, num))
        heapq.heappush(left_pq, -min(tmp, num))
        heapq.heappush(right_pq, max(tmp, num))
    else :
        tmp = [-heapq.heappop(left_pq), heapq.heappop(right_pq), num]
        tmp.sort()
        if i % 2 == 0:
            heapq.heappush(left_pq, -tmp[0])
            heapq.heappush(left_pq, -tmp[1])
            heapq.heappush(right_pq, tmp[2])
        else :
            heapq.heappush(left_pq, -tmp[0])
            heapq.heappush(right_pq, tmp[1])
            heapq.heappush(right_pq, tmp[2])
        m = -heapq.heappop(left_pq)
        print(m)
        heapq.heappush(left_pq, -m)