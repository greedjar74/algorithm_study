import sys
input = sys.stdin.readline

def DP(mask):
    # 현재 체크하는 정상 조합에 이미 방문한적 있는 경우
    if dp[mask] != -1:
        return dp[mask]

    cnt = 0
    for i in range(N):
        if mask & (2 ** i) != 0: # i번째 발전기가 정상인 경우
            cnt += 1

    # 정상인 발전기 개수가 P개 이상인 경우 -> 굳이 더 진행할 필요 없음
    if cnt >= P:
        dp[mask] = 0
        return 0
    
    ret = sys.maxsize
    # i번째 발전기로 j번째 발전기 가동
    for i in range(N):
        if mask & (2 ** i) != 0: # i번째 발전기가 정상
            for j in range(N):
                if mask & (2 ** j) == 0: # j번째 발전기가 비정상
                    ret = min(ret, A[i][j] + DP(mask+(2 ** j))) # 기존값과 i번째 발전기로 j번째 발전기를 고쳤을 때 값 중 더 작은 값을 채택

    dp[mask] = ret
    return ret

N = int(input().strip())
A = list(list(map(int, input().split())) for _ in range(N))
S = input().strip()
P = int(input().strip())

dp = [-1 for _ in range(2 ** 16)]
init_mask = 0
for i in range(N):
    if S[i] == 'Y':
        init_mask += (2 ** i)

re = DP(init_mask)
if re == sys.maxsize:
    print(-1)
else :
    print(re)