def solution(n):
    answer=0
    n1=bin(n).count('1')
    while True:
        n+=1
        if bin(n).count('1')==n1:
            answer=n
            break
    # answer=0
    # n1=len(bin(n)[2:].replace("0",""))
    # while True:
    #     n+=1
    #     if len(bin(n)[2:].replace("0",""))==n1:
    #         answer=n
    #         break
    return answer