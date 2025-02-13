def DFS(current_nums, energy):
    # 남은 개수가 2개인 경우 진행 끝 -> 넘어온 에너지 값을 그대로 다시 return한다.
    if len(current_nums) == 2:
        return energy
    
    mx = 0 # 현재 상태에서 얻을 수 있는 최대 에너지
    for i in range(1, len(current_nums)-1):
        next_nums = current_nums[:i] + current_nums[i+1:] # i번째 공을 제외한 리스트 -> 다음으로 넘겨준다.
        tmp = DFS(next_nums, energy+current_nums[i-1]*current_nums[i+1]) # i를 제외한 경우에 대해 DFS를 수행
        # mx를 최대값으로 업데이트
        if tmp > mx:
            mx = tmp
    
    return mx

n = int(input())
nums = list(map(int, input().split()))
print(DFS(nums, 0))