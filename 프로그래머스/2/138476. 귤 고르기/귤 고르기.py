def solution(k, tangerine):
    answer=0
    tan={}
    for i in tangerine:
        try:
            tan[i]+=1
        except:
            tan[i]=1
    item=sorted(tan.items(),key= lambda x:x[1],reverse=True)    
    total=0
    for i in item:
        total+=i[1]
        answer+=1
        if total>=k:
            break
    
    return answer