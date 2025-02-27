def solution(s):
    answer = [0,0]
    while True:
        n=len(s)
        s1=s.replace("0","")
        m=len(s1)
        answer[1]+=(n-m)
        s=bin(m)[2:]
        answer[0]+=1
        if s=='1':
            break
    
    
    return answer