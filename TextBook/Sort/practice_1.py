"""
* 성적이 낮은 순서로 '학생' 출력 (난이도 '하')
- N명의 학생 정보, 학생 정보는 학생의 이름과 학생의 성적으로 구분됨
- 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성
- (1 <= N <= 100,000)

- 입력 예시
2
홍길동 95
이순신 77

- 출력 예시
이순신 홍길동
"""

"""
* 해답
"""
n = int(input())

ary = []

for i in range(n):
    name, score = input().split()
    ary.append((name, int(score)))

result = sorted(ary, key= lambda student: student[1])

for i in range(n):
    print(ary[0], end=' ')
"""
* 결론
- '가장 큰 수를 K번 더하고 두 번쨰로 큰 수를 한 번 더하는 연산' 의 접근이 중요
- 정렬 알고리즘이 아닌 .sort() 라는 기본 정렬 라이브러리 함수를 사용
"""