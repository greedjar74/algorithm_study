import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
B = [(A[i], i) for i in range(N)]
B.sort(reverse=True)
total = sum(A)
m = total // 2 + 1

dp = [[False for _ in range(total+1)] for _ in range(N)]
dp[0][0] = True
dp[0][B[0][0]] = True

clean = B[0][0] if B[0][0] > m-1 else -1 # clean: 과반수를 넘으면서 클린하다는 조건을 충족하는 최대의 값 -> 초기값: B[0][0]값이 과반수를 만족하는 경우 B[0][0]로 설정
for i in range(1, N):
    for j in range(m-B[i][0], m): # i까지의 값을 사용해서 만들 수 있는 최대의 clean값 찾기 -> i-1번째 값까지 사용해서 만든 값이 과반수값 - B[i][0]보다 크거나 과반수 값보다 1 작은 경우 사용가능
        if dp[i-1][j]: # i-1번째 값까지 사용해서 j를 만들 수 있는 경우 -> 해당 값에 i번째 값을 더하면 i를 사용해서 만들 수 잇는 최대 값이 된다.
            clean = max(clean, j+B[i][0]) # clean값 업데이트

    for j in range(total+1):
        if dp[i-1][j]:
            dp[i][j] = True
            dp[i][j+B[i][0]] = True

re = list()
while clean > 0:
    for i in range(N):
        if dp[i][clean]:
            clean -= B[i][0]
            re.append(B[i][1] + 1)
            break

re.sort()
print(len(re))
print(*re)