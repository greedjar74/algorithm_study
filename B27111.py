import sys
input = sys.stdin.readline

n = int(input())
in_check = dict() # 사람이 들어가있는지 체크
re = 0

for _ in range(n):
    a, b = map(int, input().split())
    # 아직 a가 입력으로 들어온적 없는 경우
    if a not in in_check:
        in_check[a] = 0
    # 건물에 들어가는 경우
    if b == 1:
        # 건물에 a가 존재하는 경우 나온 기록이 누락된 것
        if in_check[a] == 1:
            re += 1 # re값 1증가
        in_check[a] = 1 # in_check[a]를 1으로 저장 -> a라는 사람이 들어가 있다는 의미
    # 건물에서 나오는 경우
    else :
        # a가 들어간 기록이 있는 경우
        if in_check[a] == 1:
            in_check[a] = 0 # in_check[a]를 0으로 초기화
        # a가 들어간 기록이 없는 경우 -> 기록이 누락된 것
        else :
            re += 1 # re값 1증가

# 아직 건물에 남아있는 사람 체크
# 들어간 기록만 있고 나간 기록이 없는 경우
for i in in_check.keys():
    if in_check[i] == 1:
        re += 1

print(re)