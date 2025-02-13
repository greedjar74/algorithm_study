n = int(input())
prices = []
for _ in range(n):
    price = int(input())
    prices.append(price)

prices.sort(reverse=True)
re = 0
for i in range(n):
    if (i+1) % 3 != 0:
        re += prices[i]

print(re)