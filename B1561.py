import sys

input = sys.stdin.readline

# N, M 입력
N, M = map(int, input().split())

# 운행시간 입력
times = list(map(int, input().split()))

# 놀이기구 번호 바로 구할 수 있는 경우
if N <= M:
    print(N)
else:
    # 0분부터 최대 시간까지 탐색
    left, right = 0, max(times) * N

    # 이분 탐색 구현
    while left < right:
        mid = (left + right) // 2

        # mid까지 놀이기구를 탄 아이들 수 계산
        rides = M
        for time in times:
            rides += mid // time

        # 탑승한 아이가 N명을 초과하면 시간 감소
        if rides >= N:
            right = mid
        else:
            left = mid + 1

    # 마지막 아이가 탄 놀이기구 찾기
    rides = M
    for time in times:
        rides += (left - 1) // time

    for i, time in enumerate(times):
        # 해당 놀이기구가 정확히 left 시점에 비었다면
        if left % time == 0:
            rides += 1
        # 마지막 아이가 탑승한 경우 출력
        if rides == N:
            print(i + 1)
            break