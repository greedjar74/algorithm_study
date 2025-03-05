import sys
input = sys.stdin.readline

N = int(input().strip())
A = []
B = []

for i in range(1, N+1):
    a, b = map(int, input().split())
    if (a%2==0 and b%2==1) or (a%2==1 and b%2==0):
        A.append(i)
    else :
        B.append(i)

if len(A) == 0 or len(B) == 0:
    print('NO')
else :
    print('YES')
    if len(A) > len(B):
        for i in range(len(B)):
            print(B[i], end=' ')
            print(A[i], end=' ')
        print(*A[i+1:])
    else :
        for i in range(len(A)):
            print(A[i], end=' ')
            print(B[i], end=' ')
        print(*B[i+1:])