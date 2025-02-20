mask = 18
cnt = 0
for i in range(5):
    if mask & (2 ** i) != 0:
        print(mask & (2 ** i))
        cnt += 1

print(cnt)