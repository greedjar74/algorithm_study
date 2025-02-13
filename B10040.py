n, m = map(int, input().split())
A_list = list(int(input()) for _ in range(n))
poll = [0 for _ in range(n)]

for _ in range(m):
    b = int(input())
    for i in range(n):
        if A_list[i] <= b:
            poll[i] += 1
            break

print(poll.index(max(poll)) + 1)