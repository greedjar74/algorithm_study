def DFS(current, path):
    cnt = 0
    for node, alphabet in graph[current]:
        if not visited[node]:
            path.append(alphabet)
            visited[node] = True
            DFS(node, path)
            path.pop()
        else :
            cnt += 1

    if cnt == len(graph[current]):
        paths.append(path[:])

def get_score(s1, s2):
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            if s1[j-1] == s2[i-1]:
                dp[j][i] = dp[j-1][i-1] + 1
            else :
                dp[j][i] = max(dp[j-1][i], dp[j][i-1])
    
    return dp[-1][-1]

n, m = map(int, input().split())
S = list(input())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = input().split()
    graph[int(a)-1].append((int(b)-1, c))
    graph[int(b)-1].append((int(a)-1, c))

visited = [False for _ in range(n)]
visited[0] = True
paths = []

DFS(0, [])
mx = 0

for path in paths:
    tmp = get_score(S, path)
    mx = max(mx, tmp)

print(mx)