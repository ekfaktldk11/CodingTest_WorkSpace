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
for i in range(ary_size): c_ary[array[i]] += 1

for i in range(c_size):
    for j in range(c_ary[i]):
        new_ary.append(i)

print(new_ary)