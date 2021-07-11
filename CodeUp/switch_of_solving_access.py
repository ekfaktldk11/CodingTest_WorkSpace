# 생각의 전환 ! -> 문제를 푸는 접근 방식의 전환
"""
3명의 사람이 채소가게를 각각 a일마다, b일마다, c일마다 한번 씩
방문한다면, 첫날에 3명 함께 채소가게를 들렸다면, 그 다음 함께 채소가게를
들르는 날은 첫날으로부터 며칠뒤일까?
-------------------------------------------------
여기서 최소공배수를 생각하는건 좋은데 이 문제를 최소공배수를 '계산'하는
문제로 생각하면 문제가 좀 어려워질 수 있다.

그럼, 논리적으로 접근해보자.
양의 정수 a,b,c 가 있을 때 이 세 양수의 최소공배수를 N 이라할 때
N을 논리적으로 표현해보면,
'N은 a로, b로 그리고 c로 나눴을 때 나머지가 모두 0 인 숫자.'
로 표현이 가능하다. 그리고 이 표현은 간단한 한줄의 수식으로 표현 가능하다.
'(N % a == 0) and (N % b == 0) and (N % c == 0)'
숫자를 1,2,3 ... N 위 조건을 만족할 때 까지 체크해보면 답을 구할 수 있다.

"""
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
N = 1
while(1):
    N = N + 1
    if((N % a == 0) and (N % b == 0) and (N % c == 0)):
        print(N)
        break

# 또는

a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

d = 1

while((d % a != 0) or (d % b != 0) or (d % c != 0)):
    d += 1
print(d)