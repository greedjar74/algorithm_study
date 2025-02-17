import sys
input = sys.stdin.readline

N = int(input().strip())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

road = [[True]*N for _ in range(N)]

# 플로이드 와샬 역으로
# i -> k -> j의 거리가 i -> j와 같으면 도로 i -> j는 건설할 필요가 없다.
# i -> k -> j의 거리가 i -> j보다 작으면 입력 데이터에 오류가 있는 것
# : i -> j 값은 i에서 j로 가는 경로 중 가장 짧은 값을 의미한다. 그런데 i -> k -> j가 더 작으면 i에서 j로 가는 더 짧은 경로가 존재한다는 의미
result = 0
for k in range(N):
    for i in range(N):
        if i != k:
            for j in range(N):
                if i != j and k != j:
                    if arr[i][j] == arr[i][k]+arr[k][j]:
                        road[i][j] = False
                    elif arr[i][j] > arr[i][k]+arr[k][j]:
                        result = -1

if not result:
    for i in range(N):
        for j in range(i, N):
            if road[i][j]:
                result += arr[i][j]

print(result)