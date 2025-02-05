def solution(n, lost, reserve):
    answer1,answer2=n,n
    yes=[]
    for lost_num in lost:
        if lost_num in reserve:
            yes.append(lost_num)
    for d in yes:
        reserve.remove(d)
        lost.remove(d)
            
    reserve1=sorted(reserve)
    reserve2=sorted(reserve)
    lost=sorted(lost)      

    for lost_num in lost:
        if lost_num-1 in reserve1:
            reserve1.remove(lost_num-1)
        elif lost_num+1 in reserve1:
            reserve1.remove(lost_num+1)
        else:
            answer1-=1
            
        if lost_num+1 in reserve2:
            reserve2.remove(lost_num+1)
        elif lost_num-1 in reserve2:
            reserve2.remove(lost_num-1)
        else:
            answer2-=1
        
    return max(answer1,answer2)
