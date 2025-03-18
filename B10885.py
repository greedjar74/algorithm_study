import sys
input = sys.stdin.readline

mod = 1000000007

T = int(input().strip()) # 테스트 케이스 개수
for _ in range(T):
    N = int(input().strip()) # 수열 원소 개수
    A = list(map(int, input().split())) # 수열

    B = [[]] # 0을 기준으로 나눠진 부분 수열
    for i in range(N):
        if A[i] == 0: # 현재 값이 0인 경우 부분 수열 추가
            B.append([])
        else :
            B[-1].append(A[i]) # 마지막 부분 수열에 현재 값 추가

    # 계속 값을 곱하는 경우 너무 커질 수 있다. -> 메모리 초과 발생
    # 2의 n제곱 형태로 표현
    # 원소의 값이 -2~2사이의 값이므로 초기값은 -2로 설정한다.
    answer_scale = 1 # 제곱승을 의미
    answer_sign = -1 # 음수인지 양수인지 표현

    # 모든 부분수열에 대해서 수행
    for b in B:
        if len(b) == 0: # 길이가 0이 아닌 경우만 진행
            continue
        
        # 1을 표현
        scale = 0
        sign = 1
        for i in range(len(b)): # 0번 인덱스부터 오른쪽으로 진행
            if b[i] == -2 or b[i] == 2: # -2 또는 2인 경우 2가 곱해지는 형태이므로 scale을 1 증가
                scale += 1
            if b[i] == -2 or b[i] == -1: # -2 또는 -1인 경우 부호가 반대가 된다.
                sign = -sign
            
            if sign == 1: # i번째 원소까지 사용해서 구한 값의 부호가 양수인 경우
                if answer_sign == -1: # 기존 결과 부호가 음수인 경우 -> 항상 현재 값이 더 크다
                    answer_sign = 1 # 결과 부호를 양수로 만들어준다.
                    answer_scale = scale # 결과 제곱 값을 현재 제곱 값으로 바꿔준다.
                else : # 기존 결과 부호가 양수인 경우
                    answer_scale = max(answer_scale, scale) # 제곱 값이 더 큰 값을 채택
            elif answer_sign == -1: # i번째 원소까지 사용해서 구한 값의 부호가 음수이면서 결과 부호가 음수인 경우
                answer_scale = min(answer_scale, scale) # 제곱 값이 더 작은 값을 채택

        scale = 0
        sign = 1
        for i in range(len(b)-1, -1, -1): # 가장 오른쪽 원소에서 왼쪽으로 진행
            if b[i] == -2 or b[i] == 2:
                scale += 1
            if b[i] == -2 or b[i] == -1:
                sign = -sign
            
            if sign == 1:
                if answer_sign == -1:
                    answer_sign = 1
                    answer_scale = scale
                else :
                    answer_scale = max(answer_scale, scale)
            elif answer_sign == -1:
                answer_scale = min(answer_scale, scale)

    if answer_sign == 1:
        answer = 1
        for i in range(answer_scale):
            answer *= 2
            answer %= mod
        print(answer)
    else :
        if len(B) > 1:
            print(0)
        else :
            answer = 1
            for i in range(answer_scale):
                answer *= 2
                answer %= mod
            print(-answer)