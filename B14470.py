A = int(input())
B = int(input())
c = int(input())
d = int(input())
e = int(input())

cnt = 0

if A < 0:
    cnt += -A*c + d
    A = 0

print(cnt + (B-A)*e)