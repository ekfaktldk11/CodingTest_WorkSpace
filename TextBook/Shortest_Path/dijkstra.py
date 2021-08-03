"""
* 디익스트라 알고리즘
- 한 지점에서 다른 특정 지점까지의 최단 경로를 구하는 경우
- 그리디 알고리즘이라 할 수 있음
(1). 출발 노드를 설정
(2). 최단 거리 테이블을 초기화
(3). 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
(4). 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
(5). (3) & (4) 과정 반복
"""
# (1). 간단한 디익스트라 알고리즘
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 10억으로 설정. 1e9는 실수 이므로, 정수로 설정해두기 위해 int()로 감쌈

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())

# 시작 노드 번호를 입력받기 -> (1). 의 과정
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성
graph = [[] for i in range(n + 1)] # 노드 번호는 1부터 여겨지므로 range(n + 1)
# [[], [], [], [] ... ]

# 방문한 적이 있는지 체크하는 목적의 리스트 생성
visited = [False] * (n + 1)

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = graph.append(map(int, input().split())) # a에서 b로 가는 비용이 c
    graph[a].append((b, c))

# 방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드의 번호를 반환하는 함수
def get_smallest_node():
    min_val = INF
    index = 0
    for i in range(n):
        if distance[i] < min_val and not visited:
            min_val = distance[i]
            index = i
    return index

# 디익스트라 알고리즘
def simple_dij(start):
    # -------------------(2)-------------------- #
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        # start 에서 연결된 노드까지의 거리를 distance[]에 저장 -> 얘는 초기에 출발점을 기준으로 한번만 해줘도됨
        distance[i[0]] = i[0]
    # -------------------(2)-------------------- #

    # -------------------(5)-------------------- #
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for j in range(n - 1):
        # -------------------(3)-------------------- #
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # -------------------(3)-------------------- #

        # -------------------(4)-------------------- #
        # 현재 노드와 연결된 다른 노드를 확인
        for k in graph[now]:
            cost = distance[now] + k[1] # -> k[(a,b)] 여기서 b 에 접근하려면 k[0][1] 인듯해
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[k[0]]:
                # 현재 노드를 거쳐서 가는 것을 선택 당연 비용이 더 적게드니까 !
                distance[k[0]] = cost
        # -------------------(4)-------------------- #

    # -------------------(5)-------------------- #

# 다익스트라 알고리즘 수행
simple_dij(start)

# 모든 노드로 가기 위한 최단거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 'INFINITY'를 출력
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])

'''
- 시간복잡도 : O(V^2) - V:vertex
'''