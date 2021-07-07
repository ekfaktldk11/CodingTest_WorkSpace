
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
