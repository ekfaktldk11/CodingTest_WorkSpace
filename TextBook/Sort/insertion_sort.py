# 삽입 정렬 -> 특정한 데이터를 적절한 위치에 삽입 / 필요할 때 만 swap이 이루어짐
ary = list(map(int, input().split()))

n = len(ary)

for i in range(1, n): # 0 번째 요소는 이미 정렬이 되어있다고 가정!
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복하는 문법
        if ary[j] < ary[j - 1]: # < 를 > 로 바꾸면 내림차순
            ary[j], ary[j - 1] = ary[j - 1], ary[j]
        else: # 최초위치에서 왼쪽의 요소 하나만 check 해서 그 요소 보다 후 순위에 들어갈 예정이면 더 앞부분은 볼필요도 없음
            break

print(ary)

"""
- range()의 매개 변수는 3개(start, end, step)임
- 세 번째 매개 변수인 step에 -1이 들어가면 start 인덱스부터 시작해서 "end + 1" 인덱스까지 1씩 감소
- 삽입 정렬 또한 선택 정렬과 마찬가지로 반복문의 depth 가 2 라서 O(N^2)
- 하지만 삽입 정렬은 Best case의 경우(이미 거의 정렬이 완료되어 있을 경우) 시간 복잡도는 O(N)
- 따라서 삽입 정렬은 거의 정렬되어 있는 상태로 입력이 주어지는 문제에 다른 정렬 알고리즘들 보다 유리
- O(N) for Best / O(N^2) for Avg, Worst
"""