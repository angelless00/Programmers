def solution(brown, yellow):
    answer = []
    for i in range(1,yellow+1):
        if yellow%i==0:
            if 2*(i+2)+2*(yellow/i)==brown:
                answer=[yellow//i+2,i+2]
                break
        
    return answer