def solution(s):
    x = s[0]
    same_cnt, diff_cnt = 0, 0
    answer = 0
    for i in range(len(s)):
        if s[i] == x:
            same_cnt += 1
        else:
            diff_cnt += 1
            
        if same_cnt == diff_cnt:
            answer += 1
            if i+1 < len(s):
                x = s[i+1]
            same_cnt, diff_cnt = 0, 0
    
    if same_cnt > 0 or diff_cnt > 0:
        answer += 1
            
    return answer
            