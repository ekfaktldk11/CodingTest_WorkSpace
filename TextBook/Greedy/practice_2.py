"""
* 숫자 카드 게임 (난이도 '하')
1. 숫자가 쓰인 카드들이 N * M 형태로 놓여 있다. 이때 N은 행의 개수를 의미하며, M은 열의 개수를 의미
2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택
3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 함
4. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을
고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 함
- (1 <= N, M <= 100) (1 <= 입력되는 숫자들 <= 10,000)

- 입력 예시
3 3
3 1 2
4 1 4
2 2 2

- 출력 예시
2
"""

"""
* 내 접근 방법
- 각 행마다의 최소값을 비교하여 게 중에 가장 큰 값을 가지는 행의 최소값을 도출
"""

"""
* 내 코드
"""
N, M = map(int, input().split()) # 공백을 구분으로 두 개의 정수 값을 받음

ary = []

for i in range(N): # 행의 수만큼 각 행의 요소들을 입력받음
    temp = list(map(int, input().split()))
    temp.sort() # 미리 오름차순 정렬해둠 -> temp[0] : '0번' 째 행에서의 최소값
    ary.append(temp) # ary 에 추가하여 2차원 배열 형성

max_row = 0 # 행 마다의 최소중에 최대를 가지는 행
for i in range(N - 1): # 행 마다의 비교
    if(ary[i][0] < ary[i+1][0]):
        max_row = i+1

print(ary[max_row][0])


"""
* 해답
"""
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    # 가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)

"""
* 내 풀이와 해답의 풀이 방법비교
- 두개의 반복문(depth = 1)을 이용하여 처리한것과 다르게
- 하나의 반복문과 min()과 max()를 사용하여 코드를 간소화함
"""

"""
* 결론
- '행 마다의 최소값들 중 최대를 가지는 수를 구하기' 의 접근
- array 가 있을 때 min(array) 로 해당 행렬의 최소값을 이용
- 또 max() 를 사용하여 행마다의 최소들중에 최대를 가져감 
"""