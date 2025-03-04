import sys
input = sys.stdin.readline

N = int(input().strip())
lights = list(map(int, input().split()))

for i in range(1, N, 2):
    if lights[i] == 0:
        lights[i] = 1
    else :
        lights[i] = 0

blocks = []
s = 0
for i in range(1, N):
    if lights[i] != lights[i-1]:
        blocks.append((s, i-1))
        s = i
blocks.append((s, i))

re = 0
if len(blocks) <= 3:
    re = blocks[-1][1] - blocks[0][0] + 1
else :
    for i in range(len(blocks)-2):
        tmp = blocks[i+2][1] - blocks[i][0] + 1
        re = max(re, tmp)

print(re)