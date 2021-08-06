"""
* 커리 큘럼 문제 (난이도 최상)
- 위상 정렬 문제
- 304pg 참고
"""

'''
* 해답
- 위상정렬로 접근하는 생각을 떠올리는 데에는 어렵지 않을 것 같음
- 하지만, 위상 정렬에서 각 간선에 '비용' 이라는 고려할 부분이 하나 더 추가되었을 경우 어떻게 그 부분을 고려해 줄 것이냐가 문제인데
- 위 부분에 대한 코드 구현에 어려움을 겪음
'''

from collections import deque
import copy

# 노드의 개수 입력받기
v = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]
# 각 강의 시간을 0으로 초기화
time = [0] * (v + 1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v + 1):
    data = list(map(int, input().split()))
    # 첫 번째 수는 시간 정보를 담고 있음
    time[i] = data[0]

    for x in data[1: -1]:  # 1부터 마지막 - 1까지
        indegree[i] += 1
        graph[x].append(i)


# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time)  # 밑의 max()에 time과 result를 함께 사용하기 때문에 .../ time의 값이 변경되면 result도 변경될 우려가 있어서... -> copy.deepcopy(time) 으로 해결!!
    q = deque()  # Queue

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i]) # 다이나믹 프로그래밍과에서 사용하는 d[] 와 비슷한 느낌
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in range(1, v + 1):
        print(result)


topology_sort()

"""
* 결론
- 입력받은 데이터를 다른 변수에 복사할 때 원본 데이터가 변경되면 복사한 변수도 값이 변경됨에 주의 하자
- 이 문제 같은 경우 리스트를 하나 더 복사 하여 사용하기 때문에 copy 라이브러리의 deepcopy() 함수를 사용해서 대처함
- ex)
temp = [1, 2, 3]
ary = temp
temp[1] = 10
print(ary) # [1, 10, 3]
"""