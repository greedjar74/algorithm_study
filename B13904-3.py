# 메모리를 조금 아끼는 방법
# 입력을 받으며 마감기한의 최대값을 찾아서 활용한다.
# 런타임 에러 발생..

from queue import PriorityQueue

n = int(input())
homework_list = list()
mx = 0

for _ in range(n):
    date, score = map(int, input().split())
    homework_list.append((date, score))

    if mx < date:
        mx = date

due = [[] for _ in range(mx + 1)]
for i in range(n):
    tmp = homework_list[i]
    due[tmp[0]].append(tmp[1])

pq = PriorityQueue()
re = 0

for i in range(mx, 0, -1):
    for score in due[i]:
        pq.put(-score)

    if pq.qsize() > 0:
        re += -pq.get()

print(re)