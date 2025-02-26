def solution(numbers):
    answer = ''
    numbers=[str(n) for n in numbers]
    numbers=sorted(numbers,key=lambda x:x*3,reverse=True)
    for n in numbers:
        answer+=n
    if numbers[0]=="0":
        answer="0"
    return answer