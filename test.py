import random

cnt_1 = 0
cnt_2 = 0

for i in range(100):
    r = random.randint(1, 2)
    if r == 1:
        cnt_1 += 1
    else :
        cnt_2 += 1

print(cnt_1)
print(cnt_2)