n = int(input())
in_building = set()
re = 0

for _ in range(n):
    a, b = map(int, input().split())
    # a가 들어가는 경우
    if b == 1:
        if a in in_building: # 기존에 a가 들어간 기록이 남아있는 경우
            re += 1 # 나간 기록이 누적된 것이므로 1 증가 -> 나간 기록을 만들어주는 것과 동일
        in_building.add(a) # set이기에 그냥 넣어줘도 된다.

    # a가 나가는 경우
    else :
        if a not in in_building: # 기존에 들어간 기록이 없는 경우
            re += 1 # 1 증가
        else : # 기존에 들어간 기록이 있는 경우
            in_building.remove(a) # a를 제거한다.

# 남아있는 사람의 수를 체크
re += len(in_building)
print(re)