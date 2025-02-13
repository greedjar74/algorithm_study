from collections import deque

n = int(input())
nums = list(map(int, input().split()))
c_deque = deque()
l_deque = deque()

for i in range(n):
    c_deque.append((i, nums[i]))

while len(c_deque) > 1:
    while c_deque:
        current = c_deque.popleft()
        c_size = current[1]
        tmp = c_size

        if len(l_deque) > 0 and l_deque[-1][1] <= c_size:
            tmp += l_deque[-1][1]
            l_deque.pop()

        if len(c_deque) > 0 and c_deque[0][1] <= c_size:
            tmp += c_deque[0][1]
            c_deque.popleft()
        
        l_deque.append((current[0], tmp))
    
    c_deque = l_deque
    l_deque = deque()

print(c_deque[0][1])
print(c_deque[0][0] + 1)