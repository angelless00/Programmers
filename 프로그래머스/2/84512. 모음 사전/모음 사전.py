def solution(word):
    from itertools import product
    answer = 0
    w=['A','E','I','O','U']
    words=[]
    for i in range(1,6):
        pp=product(w,repeat=i)
        for i in pp:
            a=''
            for j in i:
                a+=j
            words.append(a)
    words=sorted(words)
    answer=words.index(word)+1
    
        
        
    return answer