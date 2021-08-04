'''
* 서로소 집합 - 공통 원소가 없는 두 집합
- 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
- union(합집합) 연산 : 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
- find(찾기) 연산 : 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산

'''

# (1). 기본적인 서로소 집합 알고리즘 소스코드

# 특정 원소가 속한 집합을 찾기 (부모 노드 찾기)
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    # 두 원소의 최종 부모를 찾아서 비교 후 부모 노드 수정
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

# 노의 개수와 간선(union 연산)읜 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합 : ')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블 : ')
for i in range(1, v + 1):
    print(parent[i], end=' ')