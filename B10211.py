t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    sums = [0 for _ in range(n)]
    sums[0] = nums[0]

    for i in range(1, n):
        if sums[i-1] >= 0:
            sums[i] = sums[i-1] + nums[i]
        else :
            sums[i] = nums[i]

    print(max(sums))