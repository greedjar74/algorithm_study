import sys
input = sys.stdin.readline

S = input().strip()
N = int(input().strip())
A = list(input().strip() for _ in range(N))

n = len(S)
dp = [0 for _ in range(n)]

for i in range(n):
    for a in A:
        if len(a) <= i+1 and S[i-len(a)+1:i+1] == a:
            if len(a) == i+1: # 단어의 길이와 부분 문자열의 길이가 동일한 경우 -> 무조건 가능
                dp[i] = 1
            else :
                if dp[i-len(a)] == 1: # 뒷 부분이 a와 동일하기에 앞 부분이 가능한 경우 해당 부분 문자열은 만들 수 있다.
                    dp[i] = 1

print(dp[-1])