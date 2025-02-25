# 순서가 섞여있으면 만들 수 있음에도 못 만든다고 판단하는 경우 발생

import sys

N, M = map(int, input().split())
A = dict()
for _ in range(N):
    a, b = input().split()
    A[a] = int(b)

B = dict()
for _ in range(M):
    a, b = input().split('=')
    if a not in B:
        B[a] = list()
    B[a].append(dict())
    idx = len(B[a])-1

    tmp = b.split('+')
    for j in range(len(tmp)):
        c, d = tmp[j][0], tmp[j][1:]
        if d not in B[a][idx]:
            B[a][idx][d] = 0
        B[a][idx][d] += int(c)

key_list = list(B.keys())
for k in key_list:
    if k == 'LOVE':
        continue
    
    for i in range(len(B[k])):
        tmp = 0
        ks = list(B[k][i].keys())
        for k2 in ks:
            if k2 not in A:
                tmp = -1
                break
            tmp += A[k2] * B[k][i][k2]
        
        if tmp > -1:
            if k not in A:
                A[k] = sys.maxsize
            A[k] = min(tmp, A[k])

re = sys.maxsize
if 'LOVE' in B:
    for i in range(len(B['LOVE'])):
        tmp = 0
        for k in list(B['LOVE'][i].keys()):
            if k not in A:
                tmp = sys.maxsize
                break
            tmp += A[k] * B['LOVE'][i][k]
        re = min(re, tmp)

if 'LOVE' in A:
    re = min(re, A['LOVE'])

print(A)
print(B)

if re == sys.maxsize:
    print(-1)
elif re > 1000000000:
    print(1000000001)
else :
    print(re)