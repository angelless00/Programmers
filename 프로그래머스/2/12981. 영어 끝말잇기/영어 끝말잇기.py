def solution(n, words):
    answer = []
    dic={}
    last_word=words[0][0]
    for idx,word in enumerate(words):
        ## 한글자단어일떄
        if len(word)==1:
            if (idx+1)%n==0:
                answer=[n,(idx+1)//n]
            else:
                answer=[(idx+1)%n,(idx+1)//n+1]
            break
            
        ## 끝말잇기가 틀렷을때
        if last_word[-1]!=word[0]:
            if (idx+1)%n==0:
                answer=[n,(idx+1)//n]
            else:
                answer=[(idx+1)%n,(idx+1)//n+1]
            break
        else:
            last_word=word
            
        ##중복단어 
        
        try:
            dic[word]+=1
        except:
            dic[word]=1
        if dic[word]==2:

            if (idx+1)%n==0:
                answer=[n,(idx+1)//n]
            else:
                answer=[(idx+1)%n,(idx+1)//n+1]
            break
    if not answer:
        answer=[0,0]
        
    return answer


