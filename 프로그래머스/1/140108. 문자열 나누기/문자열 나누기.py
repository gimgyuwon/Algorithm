def solution(s):
    answer = 0
    i = 0
    while i < len(s):
        equal_cnt = 1
        not_equal_cnt = 0
        x = s[i]
        j = 0
        for j in range (i+1, len(s)):
            if s[j] == x:
                equal_cnt += 1
            else:
                not_equal_cnt += 1        
            if (equal_cnt == not_equal_cnt):
                answer+=1
                i = j + 1
                break
        else:
            answer +=1
            break
    return answer
            