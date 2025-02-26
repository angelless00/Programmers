def solution(clothes):
    answer = 0
    c={}
    for cloth,idx in clothes:
        try:
            c[idx]+=1
        except:
            c[idx]=1
    num=1
    for name in c:
        num*=(c[name]+1)
    answer=num-1
        
            
    return answer