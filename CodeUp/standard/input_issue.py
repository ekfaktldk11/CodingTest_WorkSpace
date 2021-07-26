# 1. 입력 문제 : 공백을 두고 입력된정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.
a, b = input().split()
print(a)
print(b)


# 2. 입력문제 : 24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.

a, b = input().split(':')
print(a, b, sep=':')

""" 
3. 입력문제
- 공백을 기준으로 입려되는 두 개의 value
-> a,b = input().split()
- 줄바꿔 입력되는 두 개의 value
-> 
a = input()
b = input()
"""

# 4. 입력된 문자를 16진수로 인식
n = int(input(), 16)


"""

sys.stdin.readline() 사용법
- 한 두줄 입력받는 문제들과 다르게, 반복문으로 여러줄을 입력 받아야
할 때는 input()으로 입력 받는다면 시간초과가 발생할 수 있음.

"""

# 1. 한 개의 정수를 입력받을 때

import sys

a = int(sys.stdin.readline())
# -> sys.stdin.readline() 은 한줄 단위로 입력받기 때문에,
# 개행문자가 같이 입력받아짐. ex(\n) -> 이 기행문자를 제거하기 위해서
# a = sys.stdin.readline() 로 쓰지 않고 또 정수로 사용하기 위해
# a = int(sys.stdin.readline()) 으로 사용

# 2. 정해진 개수의 정수를 한줄에 입력받을 때
a, b, c = map(int, sys.stdin.readline().split())

# -> map은 반복 가능한 객체(리스트 등)에 대해 각각의 요소들을 지정된 함수로 처리해주는 함수
# 위와 같이 사용하면 a, b, c에 대해 각각 int형으로 형변환을 할 수 있음

# 3. 임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장할 때
data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))
"""
# -> input()을 사용하여 위와 동일한 코드를 생성한 것
data = []
n = int(input())
for i in range(n):
    temp = input().split()
    for j in range(len(temp)):
        temp[j] = int(temp[j])
    data.append(temp)
"""


# 4. 문자열 n줄을 입력받아 리스트에 저장할 때
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]

# -> strip() 은 문자열 맨 앞과 맨 끝의 공백문자를 제거함
# 입력예시 :
# 코딩테스트
# 꼭 한번에 붙고 싶다
# 열공하자

print(data)
# ['코딩테스트', '꼭 한번에 붙고 싶다', '열공하자']

"""
sys.stdin.readline().strip('str') : 인자로 전달된 문자를 String의 왼쪽과 오른쪽에서 제거
sys.stdin.readline().lstrip('str') : 인자로 전달된 문자를 String의 왼쪽에서 제거
sys.stdin.readline().rstrip('str') : 인자로 전달된 문자를 String의 오른쪽에서 제거
!! 중요 !!
(1). strip 함수는(l,r 포함) 함수 인자가 없을 경우 인자로 ' ' 공백을 받기 때문에 공백을 지움
(2). strip 함수는(l,r 포함) 동일하지 않은 문자가 나올 때까지 제거함 -> 인자와 상관없는 문자가 나오면 문자 제거 중단
(3). sys 라이브러리를 사용할 때는 한 줄 입력받고 나서 rstrip() 함수를 꼭 호출해야함
왜냐하면 readline() 사용시 Enter가 줄 바꿈 기호로 입력되는데, 이 공백 문자를 제거하려면 rstrip() 함수를 사용해야함

ex)
text = ",,,,,123.....water....pp"
print(text.lstrip(',123.p'))
print(text.rstrip(',123.p'))
print(text.strip(',123.p'))

water....pp
,,,,,123.....water
water
"""