import sys
input = sys.stdin.readline

N = int(input().strip())
nums = list(map(int, input().split()))

s = [0, 0]
for i in range(N):
    if i % 2 == 0:
        s[0] += nums[i]
    else :
        s[1] += nums[i]

if N==3 and s[0] > s[1]:
    print(-1)
else :
    print(max(s)-min(s))