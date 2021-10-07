# 에라토스테네스의 체
import math
n = int(input())
sieve = [True] * (n + 1)

# n의 최대 약수가 sqrt(n) 이하이므로 i = sqrt(n)까지 검사
m = int(math.sqrt(n)) # or int(n ** 0.5)
for i in range(2, m + 1):
    if sieve[i] == True: # i 가 소수인 경우
        for j in range(i+i, n, i): # range(시작, 끝, ++) # i 이후 i의 배수들을 False 판정
            sieve[j] = False
sieve_list = [i for i in range(2, n + 1) if sieve[i] == True]
print(sieve_list)