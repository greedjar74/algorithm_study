n, k = map(int, input().split())
weights = list(map(int, input().split()))
weights.sort()
i = 0
j = n-1
cnt = 0

while i < j:
    if(weights[i] + weights[j]) <= k:
        i += 1
        cnt += 1
    j -= 1

print(cnt)