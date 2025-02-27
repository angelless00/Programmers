def solution(s):
    answer = 0
    l=[]
    for i in s:
        if len(l)==0:
            l.append(i)
        else:
            if l[-1]==i:
                l.pop()
            else:
                l.append(i)
    if len(l)==0:
        answer=1
    return answer
        
            
    
    # while True:
    #     s_set=set(s)
    #     for t in s_set:
    #         T=t+t
    #         s1=s.replace(T,"")
    #     if len(s)==len(s1):
    #         break
    #     else:
    #         s=s1
    # if len(s)==0:
    #     answer=1
    # else:
    #     answer=0
    # return answer