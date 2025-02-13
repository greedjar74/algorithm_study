N, K, A, B = map(int, input().split())
m = N // A
cnt = 0
i = 0

water = [K for _ in range(N)]

while True:
    cnt += 1
    start = A * i
    is_stop = False
    for j in range(N):
        if start <= j < (start+A):
            water[j] += B
        water[j] -= 1
        if water[j] == 0:
            is_stop = True
            break
    if is_stop:
        break

    i = (i + 1) % m

print(cnt)