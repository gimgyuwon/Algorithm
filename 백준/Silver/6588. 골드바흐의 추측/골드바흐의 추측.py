import sys

def prime_list(n):
    lst = [False] * 2 + [True] * (n-1)
    for i in range(2, int(n**0.5)+1):
        if lst[i]:
            for j in range(i*i, n+1, i):
                lst[j] = False
    return lst

def goldbach(n, prime_list):
    for a in range(3, int(n//2)+1, 2):
        b = n - a
        if prime_list[a] and prime_list[b]:
            print(f"{n} = {a} + {b}")
            return
    print("Goldbach's conjecture is wrong.")


n = []

for line in sys.stdin:
    t = line.strip()
    if t == '0':
        break
    n.append(t)

prime_list = prime_list(max(map(int, n)))

for t in map(int, n):
    goldbach(t, prime_list)