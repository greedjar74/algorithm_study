import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
right = N
p = -1

while left <= right:
    mid = (left + right) // 2
    cnt = 1
    la = nums[0]
    for i in range(1, K):
        if nums[i] - la >= mid:
            cnt += 1
            la = nums[i]
    
    if cnt >= M:
        p = mid
        left = mid + 1
    else :
        right = mid - 1

re = [0 for _ in range(K)]
re[0] = 1
cnt = 1
la = nums[0]
for i in range(1, K):
    if cnt == M:
        break
    if nums[i]-la >= p:
        re[i] = 1
        cnt += 1
        la = nums[i]

for i in re:
    print(i, end='')