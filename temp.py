import heapq

t = int(input())

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dij():
    n = int(input())

    INF = int(1e9)

    graph = []

    distance = [[INF] * n for _ in range(n)]

    def valid(x, y):
        if x >= 0 and y >= 0 and x < n and y < n:
            return True
        else:
            return False

    for i in range(n):
        temp = list(map(int, input().split()))
        graph.append(temp)

    q = []

    heapq.heappush(q, (graph[0][0], 0, 0))

    distance[0][0] = graph[0][0]

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist: continue

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not valid(nx, ny): continue
            cost = dist + graph[nx][ny]
            if distance[nx][ny] > cost:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny)) # dist 값이 들어가는게 아니라 cost값이 들어가야함 !!
    print(distance[n - 1][n - 1])

for _ in range(t): dij()
