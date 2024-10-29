def solution(t, p):
    answer = 0
    for i in range (len(t)-len(p)+1):
        substring = int(t[i:i+len(p)])
        if (substring <= int(p)):
            answer += 1
    return answer