c = int(input())
for _ in range(c):
    d, n = map(int, input().split())
    nums = list(map(int, input().split()))
    psum = [0 for _ in range(n)] # 누적합
    psum[0] = nums[0]
    for i in range(1, n):
        psum[i] = psum[i-1] + nums[i]

    re = 0
    cnt = dict() # d로 나눴을 때 발생하는 특정 나머지값이 몇 번 나왔는지 저장한다.
    cnt[0] = 1 # d로 나눠떨어지는 경우를 위해 -> 이전에 해당 값이 없어도 완전히 나눠지는 경우 re에 1을 더해줘야 한다.
    for i in range(n):
        # 이전에 없던 값인 경우
        if psum[i] % d not in cnt:
            cnt[psum[i]%d] = 0 # 1이 아닌 0인 이유: 이번에 처음 나왔으므로 기존에 있던 구역으로 만들 수 없기 때문
        re += cnt[psum[i]%d] # 결과에 cnt값을 더한다.
        cnt[psum[i]%d] += 1 # 딕셔너리에서 나머지 값에 해당하는 값에 1을 더한다.

    print(re)