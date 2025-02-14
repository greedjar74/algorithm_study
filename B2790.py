import sys
input = sys.stdin.readline

n = int(input().strip())
points = list(int(input().strip()) for _ in range(n))
points.sort()

re = 0
mx = -1
for i in range(n-1, -1, -1):
    # 자신보다 높은 랭크의 선수들 점수 중 최고 점수보다 큰 경우 -> 우승할 수 있다.
    if points[i] + n >= mx:
        re += 1
    # 자신보다 높은 랭크의 선수들 점수 중 최고 점수보다 작은 경우 -> 더이상 우승할 수 있는 경우가 없다.
    else :
        break

    mx = max(mx, points[i] + n - i) # i번째 선수 바로 다음 선수에게 남은 점수 중 가장 큰 점수를 부여 -> 매번 1씩 증가한다!

print(re)