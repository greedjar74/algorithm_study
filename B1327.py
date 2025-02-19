import sys
from collections import deque
input = sys.stdin.readline

# 리스트를 해시로 변경 -> 각 리스트를 고유의 값으로 변경해준다.
def list_to_hash(a):
    hash = 0
    for i in range(len(a)):
        hash += a[i]
        hash *= (len(a) + 1)
    return hash

# BFS
def BFS(start, e_hash):
    need_visit = deque()
    need_visit.append(start)
    s_hash = list_to_hash(start)
    visited = {s_hash}
    dist = {s_hash:0}

    while need_visit:
        current = need_visit.popleft()
        c_hash = list_to_hash(current)
        
        if c_hash == e_hash:
            return dist[c_hash]
        
        for i in range(N - K + 1):
            nxt = current[:i] + current[i:i+K][::-1] + current[i+K:]
            nxt_hash = list_to_hash(nxt)
            if nxt_hash not in visited:
                need_visit.append(nxt)
                visited.add(nxt_hash)
                dist[nxt_hash] = dist[c_hash] + 1

    return -1

N, K = map(int, input().split())
nums = list(map(int, input().split()))
sorted_nums = sorted(nums)
e_hash = list_to_hash(sorted_nums)
print(BFS(nums, e_hash))