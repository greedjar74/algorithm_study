def DFS(current):
    if len(current) == len(S):
        return current == S

    if current[-1] == 'A':
        if DFS(current[:-1]):
            return True

    if current[0] == 'B':
        if DFS(current[1:][::-1]):
            return True

    return False

S = list(input())
T = list(input())
   
if DFS(T):
    print(1)
else :
    print(0)