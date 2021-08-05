"""
* 서로소 집합을 활용한 사이클 판별
- 서로소 집합은 '무방향 그래프' 내에서의 사이클을 판별할 때 사용
- 사이클 판별
(1). 각 산서을 확인하며 두 노드의 루트 노드를 확인
 [1]. 루트 노드가 서로다르다면 두 노드에 대하여 union 연산을 수행
 [2]. 루트 노드가 서로 같다면 사이클(Cycle)이 발생한 것
(2). 그래프에 포함되어 있는 모든 간선에 대하여 (1)번 과정을 반복

- 사이클 판별 코드도 외우기 어렵지 않으니 외우길 바람!
"""

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n, m = map(int, input().split())

parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

# 사이클 발생 여부
cycle = False

for i in range(m):
    p, q = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, p) == find_parent(parent, q):
        cycle = True
        break
    else:
        union(parent, p, q) # union()을 수행함으로써 tracking을 하는 것임
if cycle:
    print('사이클이 발생 했습니다.')
else:
    print('사이클이 발생하지 않았습니다.')
"""
* union() 을 통해 tracking 을 해가면서 사이클이 발생하는지 check ~ 
"""