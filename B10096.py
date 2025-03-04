import sys
input = sys.stdin.readline

def sol(a, b):
    n = len(a)
    lcp = n
    for i in range(n):
        if a[i] != b[i]:
            lcp = i
            break
    lcs = n
    for i in range(n):
        if a[-1-i] != b[-1-i]:
            lcs = i
            break
    
    return lcp+lcs >= n

N = int(input().strip())
U = input().strip()

if N % 2 == 0:
    print("NOT POSSIBLE")
else :
    m = N // 2
    re = []
    if sol(U[:m], U[m:]):
        re.append(U[:m])
    if sol(U[m+1:], U[:m+1]):
        re.append(U[m+1:])
    
    re = list(set(re))
    if len(re) == 0:
        print("NOT POSSIBLE")
    elif len(re) == 1:
        print(re[0])
    else :
        print("NOT UNIQUE")