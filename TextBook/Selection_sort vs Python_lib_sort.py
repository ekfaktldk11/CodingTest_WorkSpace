from random import randint
import time

# 배열에 10,000개의 정수를 삽입
array = []
for _ in range(10000):
    array.append(randint(1, 100))  # 1 부터 100 사이의 랜덤한 정수

# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택 정렬 프로그램 소스코드
for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if (array[min_index] > array[j]):
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # 스왑

end_time = time.time()  # 선택 정렬 성능 측정 종료

print("선택 정렬 성능 측정:", end_time - start_time)

# 배열을 다시 무작위 데이터로 초기화

array = []
for _ in range(10000):
    array.append(randint(1, 100))

# 기본 정렬 라이브러리 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
array.sort()
# 기본은 내림차순
# sorted() : 정렬된 새로운 객체를 반환 , 리스트 뿐아니라 딕셔너리 형태도 정렬 가능 sorted({3: 'D', 2: 'B', 5: 'B', 4: 'E', 1: 'A'}) -> [1, 2, 3, 4, 5]
# sorted(array, key=setting)으로 키값도 함께 가져올 수 있음
# .sort(reverse=True) -> 오름차순

end_time = time.time()  # 기본 정렬 라이브러리 성능 측정 종료

print("기본 정렬 라이브러리 성능 측정:", end_time - start_time)

"""
선택 정렬 성능 측정: 10.980623960494995
기본 정렬 라이브러리 성능 측정: 0.0019941329956054688
"""