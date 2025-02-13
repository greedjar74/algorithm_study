import sys
input = sys.stdin.readline

def find_base(string):
    for i in range(1, len(string) + 1):
        if len(string) % i == 0:
            is_base = True
            for j in range(0, len(string), i):
                if string[:i] != string[j:j+i]:
                    is_base = False
                    break
        if is_base:
            break
    
    return string[:i]

s = input().strip()
t = input().strip()

if find_base(s) == find_base(t):
    print(1)
else :
    print(0)