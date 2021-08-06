"""
* 도시 분할 계획 (난이도 중)
- 최소 신장 트리 대표 예제 중 하나
- 300pg 참고
"""

'''
* 내 풀이 및 해답
- 접근 및 풀이 완벽했음
- 전체 그래프에서 2개의 최소 신장 트리를 만든다 -> 최소 신장 트리 하나 만들고 제일 비용이 큰 간선 하나 자르면 된다
'''
import sys

INF = int(1e9)

input = sys.stdin.readline

# 싸이클 판별을 위한 ~
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 싸이클 판별을 위한 ~
def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, input().split())

# distance = [INF] * (n + 1)
graph = []
parent = [0] * (n + 1)

# 첨엔 자기자신으로 가는 ~
for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()
result = []


for edge in graph:
    p, q = edge[1], edge[2]
    # 싸이클이 형성되면 해당 edge 무시
    if find_parent(parent, p) == find_parent(parent, q):
        continue
    # 싸이클 형성이 되지 않는다면 spanning tree의 일부에 포함시킴
    else:
        union(parent, p, q)
        result.append(edge[0])

# 전체합에서 제일 큰놈 빼기
print(sum(result) - max(result))
