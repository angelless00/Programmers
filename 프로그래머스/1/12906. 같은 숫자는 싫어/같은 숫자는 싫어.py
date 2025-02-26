def solution(arr):
    answer = []
    for idx,num in enumerate(arr):
        if idx==0:
            answer.append(num)
        else:
            if answer[-1]==num:
                continue
            else:
                answer.append(num)
        
    return answer