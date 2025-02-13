a, b, c = map(int, input().split())
cnt = dict()
mx = 0
mx_num = 0

for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            tmp = i+j+k
            if tmp not in cnt:
                cnt[tmp] = 0
            cnt[tmp] += 1
            if cnt[tmp] > mx:
                mx = cnt[tmp]
                mx_num = tmp

print(mx_num)