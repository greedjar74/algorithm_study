import sys
input = sys.stdin.readline

N = int(input().strip())
nums = list(int(input().strip()) for _ in range(N))
nums.sort()

re = 0
for i in range(1, N-1):
    min_avg = nums[0] + nums[i] + nums[i+1]
    max_avg = nums[i-1] + nums[i] + nums[-1]
    re = max(re, abs(min_avg - 3 * nums[i]))
    re = max(re, abs(max_avg - 3 * nums[i]))

print(re)