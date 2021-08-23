n, m = map(int, input().split())

house_list = []
total = 0

for _ in range(m):
    x, y, z = map(int, input().split())
    house_list.append((z, x, y))
    total += z

house_list.sort()
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

while len(house_list) > 0:
    cost, a, b = house_list.pop(0)
    if find(parent, a) == find(parent, b): continue
    else:
        union(parent, a, b)
        total -= cost

# for i in range(n):
#     for j in range(n):
#         if graph[i][j] > 0:
#             if find(parent, i) == find(parent, j):
#                 continue
#             else:
#                 union(parent, i, j)
#                 total += graph[i][j]

print(total)