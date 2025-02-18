import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    A = int(input().strip())
    N = list(set(map(int, input().split())))
    B = int(input().strip())
    M = list(set(map(int, input().split())))
    C = int(input().strip())
    K = list(set(map(int, input().split())))

    re = set()
    for a in N:
        for b in M:
            for c in K:
                tmp = str(a+b+c)
                lucky_num = True
                for i in range(len(tmp)):
                    if tmp[i] != '5' and tmp[i] != '8':
                        lucky_num = False
                        break
                if lucky_num:
                    re.add(int(tmp))

    print(len(re))