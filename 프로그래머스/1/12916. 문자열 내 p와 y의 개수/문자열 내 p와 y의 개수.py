def solution(s):
    p = 0
    y = 0
    for i in s.lower():
        if i == 'p':
            p += 1
        if i == 'y':
            y += 1
            
    return p == y