'''
* 개선된 디익스트라 알고리즘
- 기본 디익스트라는 O(V^2) 의 시간 복잡도를 가지지만
- 개선된 디익스트라 알고리즘은 O(ElogV) 의 시간 복잡도로 문제를 해결가능 / E : 간선의 개수, V : 노드의 수

(1). 출발 노드를 설정
(2). 최단 거리 테이블을 초기화 -> 개선된 디익 알고리즘엔 (2)의 과정이 좀 다름
(3). 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
(4). 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
(5). (3) & (4) 과정 반복

'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미 : 10억

# 노드의 개수, 간선의 개수를 입력받음
n, m = map(int, input().split())

# 시작 노드 번호를 입력받기
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성
graph = [[] for i in range(n + 1)]

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력
for _ in range(m):
    a, b, c = map(int(), input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

def improved_dij(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 pop -> headq 내부에서 가장 우선순위가 높은대로 알아서 정렬이됨
        dist, now = heapq.heappop(q) # (cost, 노드)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 디익스트라 알고리즘 수행
improved_dij(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 'INFINITY'를 출력
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])