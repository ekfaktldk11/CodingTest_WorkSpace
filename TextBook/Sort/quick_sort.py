# 퀵 정렬 -> 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꿈

# (1). 퀵 정렬 기본 소스코드

array = list(map(int, input().split()))

def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return
    pivot = start  # 피벗 => 첫 번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:  # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1) # 엇갈리지 않은 경우도 있기에 end point를 left가 아닌 right - 1로 해야함
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)

# (2). 파이썬의 장점을 살린 퀵 정렬 소스코드

array = list(map(int, input().split()))

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    # 둘중에 한쪽에만 <= 와 같이 '같다'의 비교연산이 들어가야 배열에 중복된 숫자가 있을시 누락시키지 않고 포함시킬 수 있기에

    # 분할 이후 왼쪽 부분과 오른쪽 부부엔서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

"""
- 퀵 정렬의 시간 복잡도에서 주목할 내용은 Avg case가 O(N*logN) 이라는 것임 # 일반적으로 컴퓨터 사이언스에서 log 는 밑을 2로 하는 log
- 피벗값의 위치가 변경되어 분할이 일어날 때마다 정확히 왼쪽 리스트와 오른쪽 리스트를 절반씩 분할한다면 ..?
- ex) 데이터의 개수 : 8
    |   [[], [], [], [], [], [], [], []]
    |   [[], [], [], []], [[], [], [], []]
h: logN [[], []], [[], []], [[], []], [[],[]]
    |   [[]], [[]], [[]], [[]], [[]], [[]], [[]], [[]]
    ------------------ w: N ---------------------------
- 다시 말해 N 이 증가할 수록 분할이 이루어지는 횟수가 기하급수적으로 감소하게 됨
- O(N*logN) for Best, Avg / O(N^2) for Worst
- 재밌는 부분은 데이터가 무작위로 입력되는 경우 퀵 정렬은 빠르게 동작하는데, 이미 데이터가 정렬되어 있는 경우에는 매우 느리게 동작
- !! 이미 데이터가 정렬되어 있는 경우 : 삽입 정렬 / 데이터가 무작위로 입력되는 경우 : 퀵 정렬 사용..!
"""

