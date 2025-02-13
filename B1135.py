# 풀이 참조함

def DFS(current):
    times = []
    for node in tree[current]:
        DFS(node)
        times.append(re[node])

    times.sort(reverse=True)

    for i in range(len(times)):
        re[current] = max(re[current], times[i] + 1 + i)

n = int(input())
nums = list(map(int, input().split()))
tree = [[] for _ in range(n)]
for i in range(1, n):
    tree[nums[i]].append(i)

re = [0 for _ in range(n)]

DFS(0)
print(re[0])