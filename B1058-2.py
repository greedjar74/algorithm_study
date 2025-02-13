# set을 활용하여 더 쉽게 풀이

n = int(input())
graph = [list(input()) for _ in range(n)]
mx = 0

for i in range(n):
    f2 = set()
    for j in range(n):
        if graph[i][j] == 'Y':
            f2.add(j)
            for k in range(n):
                if graph[j][k] == 'Y' and k != i:
                    f2.add(k)
    
    mx = max(mx, len(f2))

print(mx)