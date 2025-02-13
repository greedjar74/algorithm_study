n = int(input())
nums = list(map(int, input().split()))

D = [0 for _ in range(n)] # 왼쪽에서 오른쪽으로 진행하는 누적합
E = [0 for _ in range(n)] # 오른쪽에서 왼쪽으로 진행하는 누적합
D[0] = nums[0]
E[-1] = nums[-1]

# 왼쪽에서 오른쪽으로 누적합 수행
for i in range(1, n):
    D[i] = max(nums[i], D[i-1]+nums[i])

# 오른쪽에서 왼쪽으로 누적합 수행
for i in range(n-2, -1, -1):
    E[i] = max(nums[i], E[i+1]+nums[i])

re = max(D) # 왼쪽에서 오른쪽으로 진행하는 누적합에서 최대값 추출
# 왼쪽에서 진행해서 i-1 까지 누적합 + 오른쪽에서 진행해서 i+1 까지 누적합
# D[i-1] + E[i+1]
# 그냥 더하는 이유? i를 제거하고 좌우를 누적하지 않는 경우는 단순 누적합에서 확인할 수 있기 때문
for i in range(1, n-1):
    re = max(re, D[i-1]+E[i+1])

print(re)