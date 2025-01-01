def solution(survey, choices):
    answer = ''
    mbti={'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for i in range(len(survey)):
        case=list(survey[i])
        if choices[i]==1:
            mbti[case[0]]+=3
        elif choices[i]==2:
            mbti[case[0]]+=2
        elif choices[i]==3:
            mbti[case[0]]+=1
        elif choices[i]==5:
            mbti[case[1]]+=1
        elif choices[i]==6:
            mbti[case[1]]+=2
        elif choices[i]==7:
            mbti[case[1]]+=3
    if mbti['R']>=mbti['T']:
        answer+='R'
    else: answer += 'T'
    if mbti['C']>=mbti['F']:
        answer+='C'
    else: answer += 'F'
    if mbti['J']>=mbti['M']:
        answer+='J'
    else: answer += 'M'
    if mbti['A']>=mbti['N']:
        answer+='A'
    else: answer += 'N'
    return answer