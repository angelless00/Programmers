def solution(picks, minerals):
    answer = 0
    mineral_count={}
    k=len(minerals)//5+1
    for i in range(min(sum(picks),k)):
        mineral_5=minerals[5*i:5*(i+1)]
        mineral_count[i]=mineral_5.count('diamond')*25 + mineral_5.count('iron')*5+mineral_5.count('stone')*1
    sort_keys=sorted(mineral_count,key=lambda x:mineral_count[x],reverse=True)
    for i in sort_keys:
        if picks[0]:
            picks[0]-=1
            for mineral in minerals[5*i:5*(i+1)]:
                answer+=1
        elif picks[1]:
            picks[1]-=1
            for mineral in minerals[5*i:5*(i+1)]:
                if mineral=='diamond':
                    answer+=5
                else: answer+=1
        elif picks[2]:
            picks[2]-=1
            for mineral in minerals[5*i:5*(i+1)]:
                if mineral=='diamond':
                    answer+=25
                elif mineral=='iron':
                    answer+=5
                else: answer+=1
    return answer