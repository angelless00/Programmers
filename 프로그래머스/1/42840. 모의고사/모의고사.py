def solution(answers):
    answer = []
    man1=[1,2,3,4,5]
    man2=[2,1,2,3,2,4,2,5]
    man3=[3,3,1,1,2,2,4,4,5,5]
    cnt=[0,0,0]
    for i in range(len(answers)):
        if man1[i%(len(man1))]==answers[i]:
            cnt[0]+=1
        if man2[i%(len(man2))]==answers[i]:
            cnt[1]+=1
        if man3[i%(len(man3))]==answers[i]:
            cnt[2]+=1
    M_cnt=max(cnt)
    for index,num in enumerate(cnt):
        if num==M_cnt:
            answer.append(index+1)
    return answer