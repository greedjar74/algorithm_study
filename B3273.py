n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums_dict = dict()
for i in range(n):
    nums_dict[nums[i]] = True

re = 0
for i in range(n):
    try :
        if nums_dict[x-nums[i]]:
            re += 1
    except :
        continue

print(re // 2)