N, K = map(int, input().split())
nums = list(map(int, input().split()))
tmp = sum(nums[:K])
re = tmp
i = 0
j = K

while j < N:
    tmp = tmp + nums[j] - nums[i]
    re = max(re, tmp)
    i += 1
    j += 1

print(re)