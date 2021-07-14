
# 1. "!@#$%^&*()' 을 고대로 출력
print("\"!@#$%^&*()\'")

# "C:\Download\'hello'.py" 을 고대로 출력
print('"'+"C:\\Download\\"+"'hello'"+".py"+'"')

# 3. print("Hello\nWorld") 을 고대로 출력
# 내풀이 :
print("print("+'"'+"Hello"+"\\"+"n"+"World"+'"'+")")
# 정답 :
print("print(\"Hello\\nWorld\")")

"""
4. 
a = "apple" / b = "cake" 일때
print(a, b) 하면 결과는 apple cake 로 나옴
print(a+b) 하면 결과는 applecake로 나옴
"""

# 5. 출력 방식
a = ord(input())
a_ord = ord('a')
ary = []
for _ in range(a - a_ord + 1):
    print(chr(a_ord + _), end = " ")
    # -> print(, end = " ") -> 출력시 줄바꿈대신 공백으로 출력 end 시행 처리
    # -> print("\n") -> 이건 \n\n 과 같음
    # -> print(, end = " ") 을 사용하다가 줄바꿈을 하고 싶은경우 print("\n") 을 사용하지말고 print() 만 해줘도 됨