n = int(input())
pc_list = list(tuple(map(int, input().split())) for _ in range(n))
x = 0

for i in range(n):
    if abs(x - pc_list[i][0]) <= pc_list[i][1]:
        x += 1

print(x)