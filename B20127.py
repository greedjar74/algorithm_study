import sys
input = sys.stdin.readline

N = int(input().strip())
nums = list(map(int, input().split()))

cnt_1 = 0
idx_1 = 0
cnt_2 = 0
idx_2 = 0

for i in range(1, N):
    if nums[i-1] > nums[i]:
        cnt_1 += 1
        idx_1 = i
    if nums[i-1] < nums[i]:
        cnt_2 += 1
        idx_2 = i

k = sys.maxsize
if cnt_1 == 0:
    k = 0
elif cnt_1 == 1 and nums[0] >= nums[-1]:
    k = min(k, idx_1)
if cnt_2 == 0:
    k = 0
elif cnt_2 == 1 and nums[0] <= nums[-1]:
    k = min(k, idx_2)

if k == sys.maxsize:
    print(-1)
else :
    print(k)