def solution(genres, plays):
    answer = []
    play_num_dict={}
    play_list_dict={}
    for i,genre in enumerate(genres):
        try: 
            play_num_dict[genre]+=plays[i]
            play_list_dict[genre].append([i,plays[i]])
        except:
            play_num_dict[genre]=plays[i]
            play_list_dict[genre]=[[i,plays[i]]]
            
    sorted_key=sorted(play_num_dict,key=lambda x:play_num_dict[x],reverse=True)
    for genre in sorted_key:
        soted_play=sorted(play_list_dict[genre],key=lambda x:x[1],reverse=True)
        for play in soted_play[:2]:
            answer.append(play[0])
    
    
    return answer