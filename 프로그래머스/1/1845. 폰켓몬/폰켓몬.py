def solution(nums):
    answer = 0
    get_num=len(nums)/2
    exist_num=len(set(nums))
    answer=min(get_num,exist_num)
    return answer