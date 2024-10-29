def solution(t, p):
    p_length = len(p)
    list_t = list(t)
    answer = 0
    substring_list = []
    i = 0
    j = 0
    len_t = len(t)
    len_p = len(p)
    for i in range (len_t-len_p+1):
        temp_substring = 0
        for j in range(len_p):
            temp_substring += int(t[i+j])*(10**(len_p-j-1))
        substring_list.append(temp_substring)
        if (substring_list[i] <= int(p)):
            answer += 1
    return answer