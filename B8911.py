t = int(input())

dx = [0, 0, 1, 0, -1]
dy = [0, 1, 0, -1, 0]

for _ in range(t):
    opers = input()
    x_visited = [0]
    y_visited = [0]

    x = 0
    y = 0
    direction = 1

    for i in range(len(opers)):
        oper = opers[i]
        if oper == 'R':
            direction = direction % 4 + 1
        elif oper == 'L':
            direction = (direction - 2) % 4 + 1
        elif oper == 'F':
            x = x + dx[direction]
            y = y + dy[direction]
            x_visited.append(x)
            y_visited.append(y)
        else :
            x = x - dx[direction]
            y = y - dy[direction]
            x_visited.append(x)
            y_visited.append(y)

    x_visited = list(set(x_visited))
    y_visited = list(set(y_visited))

    x_max = max(x_visited)
    x_min = min(x_visited)
    y_max = max(y_visited)
    y_min = min(y_visited)

    re = (x_max - x_min) * (y_max - y_min)
    print(re)