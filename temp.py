n, m = map(int, input().split())

graph = []

home = []

chick = []

for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)

# 먼저 집과 치킨집을 파악
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1: home.append((i, j))
        if graph[i][j] == 2: chick.append((i, j))

