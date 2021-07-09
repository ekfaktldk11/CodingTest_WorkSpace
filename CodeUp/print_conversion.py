# 1. 16진수, 8진수 출력변환
val = input()
val_int = int(val)
print("%x"% val_int) # -> 16진수 / "%X" -> 출력 16진수를 대문자로
# print("%o"% val_int) -> 8 진수

# 2. 입력된 값을 16진수로 인식하여 해당 값을 8진수로 변환하여 출력
val = input()
val_hex = int(val, 16)
print("%o"% val_hex)

# 3. 입력된 값을 10진수 유니코드 값으로 변환후 출력

val_uni = ord(input())
print(val_uni)

# 4. 입력된 정수 값을 유니코드 문자로 출력

val_int = int(input())
print(chr(val_int))

# 여기서 집고 넘어가야할 것은 chr()는 정수값 -> 문자, ord()는 문자-> 정수값 형태로 바꿔주는 기능을 함

# 5. 입력된 정수의 부호를 바꿔 출력
val = input()
val_int = int(val)
print(-val_int)

# 6. 입력된 문자의 다음 아스키코드 문자를 출력
val = ord(input()) # 문자 -> 정수 로 변환하기위한 ord()
print(chr(val+1)) # 정수 -> 문자 로 변환하기위한 chr()

# 7. 16진수로 입력된 문자를 16진수 곱셈식으로 출력
n = int(input(), 16) # -> int(x, 16) x를 16진수로 변경
for i in range(1, 16):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep = "")
    # 또는 print("%X*%X=%X"%(n,i,n*i))

"""
위 결과 만약 입력된 문자가 'B' 라면

B*1=B
B*2=16
B*3=21
B*4=2C
.
.
.
로 출력됨
"""