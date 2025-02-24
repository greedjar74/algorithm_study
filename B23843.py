import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
B = [0 for _ in range(M)]
pos1 = 0 # 기기 인덱스

while True:
    B[0] += A[pos1] # 가장 충전시간이 긴 값을 B[0]에 추가
    pos1 += 1 # 다음 기기로 이동
    pos2 = 1 # 콘센트 인덱스

    # 모든 기기를 사용하기 전, 모든 콘센트를 사용하기 전
    while pos1 < N and pos2 < M:
        B[pos2] += A[pos1] # 현재 콘센트에 기기 추가
        pos1 += 1 # 다음 기기로 이동
        
        # 현재 콘세트에 추가한 기기들의 충전시간이 충전시간이 가장 큰 값과 동일한 시점 -> 2의 배수로 구성된 값이기에 항상 딱 맞아떨어진다.
        if B[pos2] == B[0]:
            pos2 += 1

    # 모든 기기를 모두 사용한 경우
    if pos1 == N:
        break

print(B[0])