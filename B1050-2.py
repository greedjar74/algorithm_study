# 매번 업데이트한 후 이를 가지고 다시 모든 재료에 대해서 연산을 수행하는 것을 반복한다.

N, M = map(int, input().split())
MAX_VAL = 1000000001

stuff = {}
for _ in range(N):
    name, cost = input().split()
    cost = int(cost)
    stuff[name] = cost

formulas = [input() for _ in range(M)]
for i in range(M):
    result, formula = formulas[i].split('=')
    if result not in stuff:
        stuff[result] = -1

    elements = formula.split('+')
    for e in elements:
        k = int(e[0])
        name = e[1:] 
        if name not in stuff:
            stuff[name] = -1

while True:
    update = False

    for i in range(M):
        result, formula = formulas[i].split('=')
        elements = formula.split('+')

        computable = True
        sum = 0
        for e in elements:
            k = int(e[0])
            name = e[1:]

            if stuff[name] == -1:
                computable = False
                break
            else :
                sum += k * stuff[name]
                sum = min(sum, MAX_VAL)

        if computable:
            if stuff[result] == -1 or stuff[result] > sum:
                stuff[result] = sum
                update = True
    
    if not update:
        break

if "LOVE" in stuff and stuff["LOVE"] != -1:
    print(stuff["LOVE"])
else :
    print(-1)