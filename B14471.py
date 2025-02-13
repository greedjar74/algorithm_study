n, m = map(int, input().split())
nums = []
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    if a >= n:
        cnt += 1
    else :
        nums.append(a)

nums.sort(reverse=True)
re = 0

for i in range(m-1-cnt):
    re += n - nums[i]

print(re)