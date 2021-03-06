"""
* 두 배열의 원소 교체 (난이도 '하')
- 두 개의 배열 A, B / 각각 N개의 원소로 구성 (모두 자연수)
- A,B 사이에 최대 K번의 바꿔치기를 통해 배열 A의 총합을 최대로
- (1 <= N <= 100,000) / (0 <= K <= N)
- 자세한건 182pg 참고

- 입력 예시
5 3
1 2 5 4 3
5 5 6 6 5

- 출력 예시
26
"""

"""
* 해답 (문제는 풀긴 풀었는데 주의할점 위주로...)
"""

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(k):
    if A[i] < B[i]: # !!
        A[i], B[i] = B[i], A[i]
    else:
        break

print(sum(A))

"""
* 결론
- 문제를 읽다가 자연스레 바꿔치기 전 A배열의 합이 B배열의 합보다 작다고 생각함
- A는 오름차순, B는 내림차순 정렬을 통해 k 만큼 바꿔치기를 할 때 A[i]와 B[i]를 서로 비교하여 B[i]가 클 경우에 바꿔치기를 해야한다는 점을 놓침
- 만약 바꿔치기를 하는 동안에 한번이라도 A[i]가 B[i]보다 크면 더이상의 바꿔치기는 의미가 없음. 왜냐하면 이후 A[i]는 점점 커지고 B[i]는 점점 작아지기 때문
- test case에 과대적합을 방지해야하는건 뉴럴 네트워크 뿐아니라 내 뉴런도 마찬가지인가봄
"""