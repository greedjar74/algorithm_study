t = int(input())

for _ in range(t):
    n = int(input())
    dp_0 = [1, 0]
    dp_1 = [0, 1]

    if n == 0:
        print(1, 0)
    
    elif n == 1:
        print(0, 1)
    
    else :
        for _ in range(n-1):
            dp_0 = [dp_0[1], dp_0[0] + dp_0[1]]
            dp_1 = [dp_1[1], dp_1[0] + dp_1[1]]

        print(dp_0[1], dp_1[1])