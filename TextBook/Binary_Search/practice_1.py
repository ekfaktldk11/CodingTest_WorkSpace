"""
* 부품 찾기 (난이도 '중')
- 전자 매장에 부품이 N개 / 각 부품에 정수 형태의 고유번호
- 한 손님이 M개의 '종류'의 부품을 대량으로 구매하려함
- 이 때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성하시오
- (1 <= N <= 1,000,000) / 1 <= N개의 정수, M개의 정수 <= 1,000,000 / (1 <= M <= 100,000) /

- 입력 예시
5
8 3 7 9 2
3
5 7 9

- 출력 예시
no yes yes
"""

"""
* 내 접근 방법
- n, m개의 정수를 입력받을 때 그 수가 최대 백만개, 십만개가 되니 빠른 입력을 위해 sys.stdin.readline()이용
- n 개의 정수를 입력받은 배열을 sort()를 통해 오름차순 정렬
- m 개 만큼 n_ary 안에서 binary search를 통해 출력
"""

"""
* 내 코드
"""
import sys

# 부품 개수
n = int(input())
n_ary = list(map(int, sys.stdin.readline().split()))

n_ary.sort()

# 주문
m = int(input())
m_ary = list(map(int, sys.stdin.readline().split()))

def b_search(target, start, end):
    mid = (start + end) // 2
    if start > end:
        print('no', end=' ')
        return
    elif n_ary[mid] < target:
        b_search(target, mid + 1, end)
    elif n_ary[mid] > target:
        b_search(target, start, mid - 1)
    else:
        print('yes', end=' ')
        return

for i in range(m):
    b_search(m_ary[i], 0, n - 1)

"""
* 해답
"""
# N
n = int(input())
# 가게에 이는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록 - ex) {2, 3, 7, 8, 9} 집합 자료형 자동으로 오름차순 정렬됨
array = set(map(int, input().split()))
# !!!!!
# array = set(map(int, sys.stdin.readline().split())) 로 해도 밑의 함수가 돌아가고 답도 제대로 나옴.
# 이게 아마도 파이썬 버전에 따라 되는게 있고 안되는게 있을거라 예상되는데 3.8 은 됨. 교재는 3.7이 기준이라 ..

# M
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')

"""
* 내 풀이와 해답의 풀이 방법비교
- 내 풀이는 이진 탐색 함수를 만들어 풀이함
- 해답은 간단히 집합 자료형을 통해 if i in array 로 있는지 없는지 확인가능 -> 파이썬의 장점중 하나
- 내 답도 틀린건 아니지만 해답 쪽이 훨씬 가독성이나 코드 간결함에 있어서 장점이 있음
- 교재에는 이진탐색, 계수정렬 로 문제를 해결하는 코드도 담겨있음
- 197p.g 확인
"""

"""
* 결론
- '가장 큰 수를 K번 더하고 두 번쨰로 큰 수를 한 번 더하는 연산' 의 접근이 중요
- 정렬 알고리즘이 아닌 .sort() 라는 기본 정렬 라이브러리 함수를 사용
"""