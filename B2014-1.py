# 숫자를 1씩 증가시키며 수행한다. -> 시간초과 발생

m, n = map(int, input().split())
nums = list(map(int, input().split()))

possible = dict()
for num in nums:
    possible[num] = True

current = min(nums)
cnt = 0

while cnt < n:
    if current in possible:
        cnt += 1
    else :
        for num in nums:
            if (current % num == 0) and ((current // num) in possible):
                possible[current] = True
                cnt += 1
                break
        
    current += 1

print(current - 1)