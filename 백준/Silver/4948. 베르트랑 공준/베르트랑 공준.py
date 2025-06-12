import sys

input = sys.stdin.read().strip().splitlines()
nums = list(map(int, input[:-1]))

# 숫자 별 소수 갯수 리스트
max = 123456 * 2 + 1
# 1은 소수 아님
isPrime = [False] + [True]*max

for i in range(2, int(max**0.5)+1):
    if isPrime[i]:
        for j in range(i*i, max+1, i):
            isPrime[j] = False

primeCnt = [0]*(max+1)
count = 0
for i in range(max + 1):
    if isPrime[i]:
        count+= 1
    primeCnt[i] = count

for n in nums:
    print(primeCnt[2*n] - primeCnt[n])
