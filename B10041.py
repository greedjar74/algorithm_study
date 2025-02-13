w, h, n = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

re = 0
for i in range(1, n):
    start = points[i-1]
    next = points[i]
    if (start[0] < next[0] and start[1] < next[1]) or (start[0] > next[0] and start[1] > next[1]):
        re += max(abs(start[0] - next[0]), abs(start[1] - next[1]))

    else :
        re += abs(start[0] - next[0]) + abs(start[1] - next[1])
    
    print(re)

print(re)