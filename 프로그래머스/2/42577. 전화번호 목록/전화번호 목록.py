def solution(phone_book):
    answer = True
    phone_book=sorted(phone_book)
    for idx,num in enumerate(phone_book[:-1]):
        if num == phone_book[idx+1][:len(num)]:
            answer=False
    return answer