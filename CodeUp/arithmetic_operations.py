# 1. 거듭제곱 **
a, b = input().split()
print(int(a)**int(b))

# 2. 나눈몫 구하기
a, b = input().split()
print(int(a)//int(b))

# 3. 나눈 나머지 구하기
a, b = input().split()
print(int(a)%int(b))

# 4. 실수 반올림
val = float(input())
print(format(val, ".2f")) # -> 소수점 둘째짜리까지 ex. 2.1235 -> 2.12)
