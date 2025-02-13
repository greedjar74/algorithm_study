N, m, M, T, R = map(int, input().split())
current = m
t = 0
cnt = 0

if (M-m) < T:
    print(-1)
else :
    while cnt < N:
        if current + T <= M:
            current += T
            cnt += 1
        else :
            current = max(m, current - R)
        t += 1
    
    print(t)