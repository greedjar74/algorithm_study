n = int(input())
nums = list(map(int, input().split()))
nums.sort()

re = 0

for i in range(n):
    tmp = nums[:i] + nums[i+1:]
    left = 0
    right = len(tmp) - 1

    while left < right:
        s = tmp[left] + tmp[right]

        if s == nums[i]:
            re += 1
            break
        elif s > nums[i]:
            right -= 1
        else :
            left += 1

print(re)