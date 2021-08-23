import heapq

n, m = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((1, b))
    graph[b].append((1, a))

distance = [INF] * (n + 1)

def dij(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: continue

        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))

dij(1)
max_val = max(distance[2:])
max_list = []
for i in range(2, n + 1):
    if distance[i] == max_val:
        max_list.append(i)

max_list.sort()
print(max_list[0], end=' ')
print(max_val, end=' ')
print(len(max_list))