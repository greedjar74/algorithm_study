x, y = map(int, input().split())
s = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
tmp = y - 1

for i in range(x):
    tmp += s[i]

tmp %= 7

if tmp == 0:
    print("MON")
elif tmp == 1:
    print("TUE")
elif tmp == 2:
    print("WED")
elif tmp == 3:
    print("THU")
elif tmp == 4:
    print("FRI")
elif tmp == 5:
    print("SAT")
else :
    print("SUN")