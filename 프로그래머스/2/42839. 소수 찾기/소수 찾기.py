from itertools import permutations

def isprime(n):
    isit=True
    n=int(n)
    n1=int(n**(1/2))
    if n==1:
        isit=False
    for i in range(2,n1+1):
        if n%i==0:
            isit=False
            break
    
    return isit
    

def solution(numbers):
    answer = 0
    num_set=set()
    for i in range(1,len(numbers)+1):
        for num in permutations(numbers,i):
            a=''
            for nn in num:
                a+=nn
            if a[0]!='0':
                num_set.add(a)
    for i in num_set:
        if isprime(i):
            answer+=1
    return answer