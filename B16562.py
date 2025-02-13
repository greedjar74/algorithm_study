n, m, p = map(int, input().split())
prices = list(map(int, input().split()))
prices.insert(0, 0)

graph = [i for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    a_p = graph[a]
    b_p = graph[b]

    if a_p != b_p:
        mn_price = min(prices[a_p], prices[b_p])
        if a_p > b_p:
            prices[b_p] = mn_price
            for i in range(1, n+1):
                if graph[i] == a_p:
                    graph[i] = b_p
        else :
            prices[a_p] = mn_price
            for i in range(1, n+1):
                if graph[i] == b_p:
                    graph[i] = a_p

top_nodes = set(graph[1:])
need_price = 0
for i in top_nodes:
    need_price += prices[i]

if p < need_price:
    print('Oh no')

else :
    print(need_price)