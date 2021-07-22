# 계수 정렬 -> 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 경우 사용 (선택, 삽입, 퀵과 다르게 비교기반이 아님!)
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = list(map(int, input().split()))

ary_size = len(array)

#모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
c_ary = [0] * (max(array) + 1)

c_size = len(c_ary)

# 계수 정렬될 배열
new_ary = []

# 각 데이터에 해당하는 인덱스의 값 증가
for i in range(ary_size): c_ary[array[i]] += 1 # 총 연산 회수 : N번 시행

for i in range(c_size): # depth 는 2 지만 결국 연산을 수행하는 총 회수는 K로 고정
    for j in range(c_ary[i]): # N
        new_ary.append(i)

print(new_ary)

"""
- 계수 정렬의 시간 복잡도 O(N+K) / K : 제일 큰 숫자
- 하지만 예를들어 데이터가 0, 999,999 단 2개만 존재할 때, 리스트의 크기가 100만 개가 되도록 선언해야 함 -> 이 경우 효율 떡락!
- !! 시간복잡도를 계산할 때에는 반복문의 depth만 보고 판단하는 것이 아닌 depth 가 몇이든 총 얼만큼의 연산 수행을 하는지 check를 해야함
- !! depth가 2 일때 반복문만 보면 O(n^2) 처럼 보이지만 어느 반복에서는 연산을 수행을 안할 수도 있기에 ... but, if 같은 조건문 연산은 반드시 수행됨 
"""