import sys

n = int(input())
m = int(input())
nums = list(map(int, input().split()))
mx_num = max(nums)

poll = [0 for _ in range(mx_num + 1)]
first_in = [0 for _ in range(mx_num + 1)]
cnt = 0

for i in range(m):
    num = nums[i]
    if cnt < n:
        if poll[num] == 0:
            first_in[num] = i+1
        poll[num] += 1
        cnt += 1

    elif poll[num] > 0:
        poll[num] += 1

    else :
        mn = sys.maxsize
        mn_in = sys.maxsize
        for j in range(1, mx_num+1):
            if poll[j] > 0 and mn > poll[j]:
                mn = poll[j]
                mn_in = first_in[j]
                mn_idx = j
            elif mn == poll[j]:
                if mn_in > first_in[j]:
                    mn_in = first_in[j]
                    mn_idx = j
        
        poll[mn_idx] = 0
        first_in[mn_idx] = 0
        poll[num] += 1
        first_in[num] = i+1

for i in range(1, mx_num+1):
    if poll[i] > 0:
        print(i, end=' ')