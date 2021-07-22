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

result = sorted(ary, key=lambda student: student[1])

for i in range(n):
    print(result[i][0], end=' ')
"""
* 결론
- 학생의 정보가 최대 100,000개 까지 입력될 수 있으므로 최악의 경우 O(N*logN)을 보장해야함
- sorted() 를 사용하되, lambda를 이용하여 정렬 기준설정
"""