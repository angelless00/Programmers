def solution(s, skip, index):
    answer = ''
    alpabet='abcdefghijklmnopqrstuvwxyz'
    skip_alpabet=[al for al in alpabet if al not in skip]
    for unch in s:
        answer+=skip_alpabet[(skip_alpabet.index(unch)+index)%len(skip_alpabet)]
    
    return answer