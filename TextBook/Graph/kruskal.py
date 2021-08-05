"""
* 신장 트리
- 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 (Tree의 성립 조건 중 하나)
"""

"""
- 크루스칼 알고리즘 (최소 신장 트리)
(1). 간선 데이터를 비용에 따라 오름차순으로 정렬
(2). 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
    [1]. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킴
    [2]. 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않음
(3). 모든 간선에 대하여 (2)번 과정을 반복
"""
# Cycle 판별을 위한 disjoint set 의 함수 중 하나인 find_parent
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# Cycle 판별을 위한 disjoint set 의 함수 중 하나인 union(union_parent)
def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())

# 부모 테이블 초기화
parent = [0] * (v + 1)

# 모든 간선을 담을 리스트
edges = []
# 최종 비용
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b)) # !! key_point

# 간선을 비용순으로 정렬 O(ElogE) / E : 간선의 수
edges.sort() # !! key_point -> 크루스칼 알고리즘에서 시간이 가장 오래 소요되는 부분이 간선을 정렬하는 작업임임
# 간선을 하나씩 확인하며
for edge in edges: # !! key_point
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += cost

print(result)