import sys
from queue import PriorityQueue # 우선순위 큐 -> 작은 값 부터 추출해준다.

T = int(input())

for _ in range(T):
    Q = int(input())

    min_pq = PriorityQueue()
    max_pq = PriorityQueue()
    count = dict()

    for _ in range(Q):
        t, v = input().split()
        v = int(v)

        if t == 'I':
            min_pq.put(v)
            max_pq.put(-v) # 큰 수부터 뽑기위해 -를 붙인다. -> PriorityQueue는 작은 값을 먼저 뽑기 때문
            if v not in count:
                count[v] = 0
            count[v] += 1
        if t == 'D':
            if v == 1:
                while max_pq.qsize() != 0:
                    x = -max_pq.get() # 가장 큰 수를 하나 뽑는다.
                    # 뽑을 수 있는 값인지 검사 -> 가능하다면 반복 종료
                    if count[x] != 0:
                        count[x] -= 1
                        break

            else :
                while min_pq.qsize() != 0:
                    x = min_pq.get()
                    if count[x] != 0:
                        count[x] -= 1
                        break

    mx = -1 * sys.maxsize
    mn = sys.maxsize

    while max_pq.qsize() != 0:
        x = -max_pq.get()
        if count[x] != 0:
            mx = x
            break
    while min_pq.qsize() != 0:
        x = min_pq.get()
        if count[x] != 0:
            mn = x
            break

    if mx == -1 * sys.maxsize:
        print("EMPTY")
    else :
        print(mx, mn)