def solution(progresses, speeds):
    answer = []
    left_progresses=[100-i for i in progresses]
    left=[]
    for idx,num in enumerate(left_progresses):
        if num%speeds[idx]==0:
            left.append(num//speeds[idx])
        else:
            left.append(num//speeds[idx]+1)
    n=0
    
    for i in left:
        if n>=i:
            answer[-1]+=1
        else:
            answer.append(1)
            n=i
        
    return answer