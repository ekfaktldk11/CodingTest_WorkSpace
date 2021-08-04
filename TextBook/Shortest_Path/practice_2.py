'''
* 전보 문제 (난이도 상)
- 262.pg 참고
- N : 도시의 수 / M : 경로의 수 / C : 메세지를 보내고자하는 도시 / Z : 메시지가 전달되는 시간
- (1 <= N <= 30,000) / (1 <= M <= 200,000) / (1 <= C <= N) / (1 <= Z <= 1,000)

- 입력 예시
3 2 1
1 2 4
1 3 2

- 출력 예시
2 4
'''

'''
* 해답
'''

# 도시의 수 n / 통로의 수 m / 메시지를 보내고자 하는 도시 c
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, r = map(int, input().split())
    graph[a].append((b, r))

start = c

def dik(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 pop -> headq 내부에서 가장 우선순위가 높은대로 알아서 정렬이됨
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시 / dist 보다 큰값을 가질 경우엔 dist 값으로 더 짧은 길을 찾을 수 있으니... < INF 가 아니라 < dist
        if distance[now] < dist: continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dik(start)

count = 0
max_time = 0

for i in range(1, n + 1):
    if distance[i] != INF:
        count += 1
        if distance[i] > max_time:
            max_time = distance[i]

print(count - 1, max_time, sep=" ")

'''
* 결론
- 디익스트라 알고리즘의 응용문제
- 응용 문제라고 할 것도 없이 거의 디익스트라 문제랑 똑띠
- N, M 의 범위가 크기 때문에 우선순위 큐를 이용하여 디익스트라 알고리즘을 작성해야 함
- 개선된 디익스트라 소스코드(min-heap을 이용하는)를 외워두자 !
'''