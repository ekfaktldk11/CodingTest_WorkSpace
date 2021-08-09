"""
* 만들 수 없는 금액 (난이도 '하', 30분, 1초, 128MB) / 314pg
- N개의 동전을 이용하여 만들수 없는 양의 정수 금액 중 최솟값을 구하시오
- (1 <= N <= 1,000) / 각 화폐 단위는 1,000,000 이하의 자연수

- 입력예시
5
3 2 1 1 9

- 출력 예시
8
"""

"""
* 내 접근 방법
- 루프문을 사용하여 target을 1 씩 증가하면서 주어진 동전으로 해당 target의 금액을 만들 수 있는지 check 하려 함
- 하지만 위 의 접근 방법을 구현하기 어려 웠음
"""

"""
* 내 풀이 (틀림)
"""

n = int(input())
coin = list(map(int, input().split()))

coin.sort()

money = 1

flag = True

while flag:
    current = 0
    # 뭘 의미하는지도 내가 봐도 모르겠다
    for co in coin:
        temp = current + co
        if temp == money:
            break
        elif temp > money:
            flag = False

"""
* 해답
"""

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력

"""
* 해답의 접근방법
- 1 부터 target - 1 까지의 모든 금액을 만들 수 있다고 가정
- 만약 target 금액을 만들 수 있다면, target 값을 업데이트하는(증가시키는) 방식을 이용함
- 매번 target인 금액도 만들 수 있는지(== 현재 확인하는 동전의 단위가 target 이하인지)
"""

"""
* 해답의 접근방법에 대한 내 해석
- target 이라는 것을 하나의 돈 뭉치 또는 새로운 화폐 단위 라고 생각하자
- 다음에 확인하는 동전의 크기가 이 화폐 단위보다 작아야 (target + x) 라는 새로운 화폐 단위를 만들 수 있는 것임
- 1 ~ target_1 / 1 ~ target_2 / 1 ~ target_3 ... 이렇게 만들 수 있는 돈의 단위를 업데이트 해나가는 것임
- 현재 확인하는 동전의 단위보다 target이 더 큰 값을 가지면 결국 해당 target에서 1을 뺀 값까지의 양의 정수 돈밖에 만들 수 없는 것임 
"""

## !! 그냥 외우자 !!
## 진짜 아무리 이해하려해도 이해가 안되네 증말...