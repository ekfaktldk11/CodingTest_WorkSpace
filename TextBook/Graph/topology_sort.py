"""
* 위상정렬

"""
from collections import deque

# 노드의 개수와 간선의 개수를 입력받기
n, m = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
degree = [0] * (n + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(n + 1)]
# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)  # 정점 A에서 B로 이동 가능
    degree[b] += 1  # 진입차수를 1 증가


# 위상 정렬 함수
def topo_sort():
    # 알고리즘 수행 결과를 담을 리스트
    result_seq = []
    # 큐 기능을 위한 deque 라이브러리 사용
    q = deque()
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1): # key_point!! range(노드의수) (o) / range(간선의수) (x)
        if degree[i] == 0:
            q.append(i)
    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()  # 큐에서 원소 꺼내기
        result_seq.append(now)
        # 해당원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            degree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if degree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in result_seq:
        print(i, end=' ')


topo_sort()