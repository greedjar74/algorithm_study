import sys
input = sys.stdin.readline

def sol(a, b, c):
    if b == 1:
        return a % c
    
    x = sol(a, b//2, c) ** 2 % c
    if b % 2 == 1:
        x = x * a % c
    
    return x

A, B, C = map(int, input().split())
print(sol(A, B, C))