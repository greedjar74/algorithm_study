import sys
from collections import deque
input = sys.stdin.readline

S = list(input().strip())
n = len(S)
queue = deque()
for i in range(n):
    if S[i] == 'B':
        queue.append(i)

re = 0
for i in range(n):
    if S[i] == 'C':
        if len(queue) != 0 and queue[0] < i:
            re += 1
            queue.popleft()

for i in range(n-1, -1, -1):
    if S[i] == 'A':
        if len(queue) != 0 and queue[-1] > i:
            re += 1
            queue.pop()

print(re)