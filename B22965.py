import sys
input = sys.stdin.readline

N = int(input().strip())
nums = list(map(int, input().split()))

cnt = 0
for i in range(1, N):
    if nums[i] < nums[i-1]:
        cnt += 1

if cnt == 0:
    print(1)
elif cnt == 1 and nums[0] > nums[-1]:
    print(2)
else :
    print(3)