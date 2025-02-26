import sys
input = sys.stdin.readline

N = int(input().strip())
nums = list(map(int, input().split()))

s = sum(nums)
tmp = 0
for num in nums:
    tmp += num**2

print((s**2 - tmp)//2)