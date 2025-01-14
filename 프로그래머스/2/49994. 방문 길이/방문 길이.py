def solution(dirs):
    answer = 0
    move=[]
    location=[0,0]
    last_location=[0,0]
    for i in dirs:
        if i=='U':
            if location[1]!=5:
                location[1]+=1
                if ((last_location,location) not in move) & ((location,last_location) not in move):
                    answer+=1
        elif i=='D':
            if location[1]!=-5:
                location[1]-=1
                if ((last_location,location) not in move) & ((location,last_location) not in move):
                    answer+=1
        elif i=='R':
            if location[0]!=5:
                location[0]+=1
                if ((last_location,location) not in move) & ((location,last_location) not in move):
                    answer+=1
        else:
            if location[0]!=-5:
                location[0]-=1
                if ((last_location,location) not in move) & ((location,last_location) not in move):
                    answer+=1
        move.append((last_location,location.copy()))
        last_location=location.copy()
        
    return answer


