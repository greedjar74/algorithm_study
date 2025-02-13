import sys
input = sys.stdin.readline

S = input().strip()
n = len(S)
tmp = list()

for i in range(n):
    tmp.append(S[i])
    if i >= 3:
        if tmp[len(tmp)-4:len(tmp)] == ['P', 'P', 'A', 'P']:
            tmp[len(tmp)-4:len(tmp)] = ['P']

if tmp == ['P']:
    print("PPAP")
else :
    print("NP")