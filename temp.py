n, m = map(int, input().split())

graph = []

for _ in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)

city_list = list(map(int, input().split()))

parent = [0] * n

for i in range(n):
    parent[i] = i

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

# 일단 전부 union 시켜서 이음
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(parent, i, j)

# 여행 계획에 있는 모든 노드들의 parent가 다르면 여행계획대로 이동 불가
master = find(parent, city_list[0])
flag = True
for node in city_list[1:]:
    if find(parent, node) != master:
        print('NO')
        flag = False
        break

if flag: print('YES')