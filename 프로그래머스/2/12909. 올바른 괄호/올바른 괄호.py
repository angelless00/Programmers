def solution(s):
    answer = True
    cnt=[]
    try:
        for i in s:
            if i=="(":
                cnt.append(0)
            elif i==")":
                cnt.pop()
    except:
        answer=False
    if answer and (len(cnt)==0):
        answer=True
    else:
        answer=False


    return answer