def solution(operations):
    que=[]
    for oper in operations:
        oper=oper.split(' ')
        if oper[0]=='I':
            que.append(int(oper[1]))
        elif oper[1]=='1':
            try:
                que.remove(max(que))
            except:
                continue
        else:
            try:
                que.remove(min(que))
            except:
                continue
    if len(que):
        answer=[max(que),min(que)]
    else:
        answer=[0,0]
    return answer