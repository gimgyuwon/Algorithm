def solution(s):
    answer = True
    p = []
    y = []
    for i in s:
        if i.lower() == 'p':
            p.append('p')
        if i.lower() == 'y':
            y.append('y')
    
    if (len(p) == len(y)) :
        answer = True
    else :
        answer = False
    return answer