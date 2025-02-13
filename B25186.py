n = int(input())
nums = list(map(int, input().split()))

total = sum(nums)
if total != 1 and max(nums) > total / 2:
    print("Unhappy")
else :
    print("Happy")