# 리스트를 활용하여 쉽게 풀이가능!
# 패스트캠퍼스 [초격차 패키지 : 2024 네카라쿠배 취업 끝장내는 파이썬 코딩테스트 마스터] Part 2 - Ch 02 - 05번

n, l, d = map(int, input().split())

time_check = [True for _ in range(4000)]
s = 0

for _ in range(n):
    for i in range(s, s+l):
        time_check[i] = False
    s += l + 5

check_time = 0
while True:
    if time_check[check_time] == True:
        print(check_time)
        exit(0)
    check_time += d