import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

psum = [0 for _ in range(N)]
psum[0] = nums[0]
for i in range(1, N):
    psum[i] = psum[i-1] + nums[i]

psum.sort(reverse=True)
print(sum(psum[:K]))