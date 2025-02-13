import sys

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

x_plus_y = []
y_minus_x = []

for i in range(n):
    x, y = points[i]
    x_plus_y.append(x+y)
    y_minus_x.append(y-x)

re1 = max(x_plus_y) - min(x_plus_y)
re2 = max(y_minus_x) - min(y_minus_x)

print(max(re1, re2))