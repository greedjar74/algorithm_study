n, l = map(int, input().split())
ligths = [list(map(int, input().split())) for _ in range(n)]

x = 0
time = 0
for i in range(n):
    gap = ligths[i][0] - x
    time += gap
    tmp = time % (ligths[i][1] + ligths[i][2]) - ligths[i][1]
    if tmp < 0:
        time -= tmp
    x = ligths[i][0]

print(time + l - x)