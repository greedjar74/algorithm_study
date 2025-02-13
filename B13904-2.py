# 우선순위 큐를 활용하여 풀이
# 런타임에러 발생..

from queue import PriorityQueue

n = int(input())
due = [[] for _ in range(1001)] # 특정 시점까지 끝내야 되는 값들을 저장하는 리스트

for _ in range(n):
    d, w = map(int, input().split())
    due[d].append(w) # d까지 마감해야 되는 과제들을 due[d]에 추가한다.

pq = PriorityQueue()
re = 0
for i in range(1000, 0, -1):
    for w in due[i]: # 현재 마감기한에 해당하는 모든 값들을 넣어준다.
        pq.put(-w) # 매번 최대값을 뽑기위해 -를 붙여서 넣어준다. -> PriorityQueue는 작은값을 뽑아주므로 양수에서 가장 큰 값은 음수에서 가장 작은값이 되고 매번 가장 큰 값이 뽑히는 원리
    
    if pq.qsize() > 0:
        re += -pq.get() # 가장 리워드가 큰 값을 뽑아 결과에 추가한다.

print(re)