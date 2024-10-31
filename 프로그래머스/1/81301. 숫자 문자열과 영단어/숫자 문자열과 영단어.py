def solution(s):
    table = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    word = ""
    ans = ""
    for i in s:
        cur_word = i
        if (cur_word.isnumeric()):
            ans += cur_word
        else:
            word += cur_word
            if word in table:
                ans += str(table.index(word))
                word=""
    return int(ans)
                    