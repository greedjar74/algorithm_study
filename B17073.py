import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(current):
    for node in graph[current]:
        if not visited[node]:
            real_graph[current].append(node)
            visited[node] = True
            DFS(node)

# 굳이 할 필요 없음
def get_prob(current):
    global re, cnt

    if len(real_graph[current]) > 0:
        nxt_prob = prob[current] / len(real_graph[current])
        prob[current] = 0
        for node in real_graph[current]:
            prob[node] = nxt_prob
            get_prob(node)
    else :
        re += prob[current]
        cnt += 1

N, W = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

real_graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
visited[1] = True
DFS(1)

prob = [0 for _ in range(N+1)]
prob[1] = W
re = 0
cnt = 0
get_prob(1)
print(re/cnt)