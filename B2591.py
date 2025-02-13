S = input()
D = [0 for _ in range(len(S) + 1)]
D[0] = 1

for i in range(1, len(S) + 1):
    D[i] = 0
    # 마지막 숫자를 따로 사용
    if S[i-1] != '0': # 0은 따로 사용할 수 없다.
        D[i] += D[i-1]
    # 두 숫자를 붙여서 사용
    # 길이가 2이상, 첫 번째 숫자가 0이 아닌 경우, 34보다 작은 경우에 만들 수 있다.
    if i >= 2 and S[i-2] != '0' and int(S[i-2:i]) <= 34:
        D[i] += D[i-2]

print(D[-1])