def solution(want, number, discount):
    from collections import Counter
    answer = 0
    for start in range(len(discount)-9):
        buy=discount[start:start+10]
        buy=Counter(buy)
        ok=True
        for idx,m in enumerate(want):                
            try:
                if buy[m]>=number[idx]:
                    continue
                else:
                    ok=False
                    break
            except:
                ok=False
                break
        if ok:
            answer+=1
                
                
    return answer