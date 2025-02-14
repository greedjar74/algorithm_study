# python3 불가능 -> 시간초과 발생 
# pypy3 가능

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    dist = []
    for i in range(1, n):
        dist.append(nums[i] - nums[i-1])

    cnt = 0
    for i in range(1, n-1):
        left = i-1
        right = i
        l_tmp, r_tmp = dist[left], dist[right]
        while left >= 0 and right < len(dist):
            if l_tmp == r_tmp:
                cnt += 1
                left -= 1
                right += 1
                if left >= 0:
                    l_tmp += dist[left]
                if right < len(dist):
                    r_tmp += dist[right]
            elif l_tmp < r_tmp:
                left -= 1
                if left >= 0:
                    l_tmp += dist[left]
            else :
                right += 1
                if right < len(dist):
                    r_tmp += dist[right]

    print(cnt)