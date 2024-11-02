def haligarli(n):
    card_dic = {
        'STRAWBERRY': 0,
        'BANANA': 0,
        'LIME': 0,
        'PLUM': 0
    }
    for _ in range(0, n):
        card = input().split(" ")
        card_dic[card[0]] += int(card[1])
    if 5 in card_dic.values():
        return "YES"
    return "NO"


n = int(input())
print(haligarli(n))
