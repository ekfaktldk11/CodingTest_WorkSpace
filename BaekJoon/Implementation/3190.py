'''
- 뱀
- https://www.acmicpc.net/problem/3190
'''

# 내 풀이 (힌트 얻고 해결 ㅠ)
from collections import deque

def terminate(x, y, snake):
    if x < 0 or y < 0 or x >= n or y >= n or (x, y) in snake:
        return True
    return False

n = int(input())
graph = [[0] * n for _ in range(n)]
k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1

count = 0
c_ary = ['N'] * 10001
l = int(input())
for _ in range(l):
    t, dir = map(str, input().split())
    c_ary[int(t)] = dir

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

d = 1;x = 0;y = 0;snake = [];snake.append((x, y))  # 시작 방향 동쪽, 시작 지점
q = deque(snake)
while True:
    x = x + dx[d]
    y = y + dy[d]
    count += 1
    if terminate(x, y, q):
        print(count)
        break
    q.append((x, y))

    if graph[x][y] != 1: q.popleft()
    else: graph[x][y] = 0 ### 하 ... 뱀이 사과를 먹었는데 사과를 없애는 코드를 넣어야죠...
    if c_ary[count] == 'D':
        d += 1
        if d == 4: d = 0
    elif c_ary[count] == 'L':
        d -= 1
        if d == -1: d = 3


'''
# 결론
- 위 문제 처럼 배열에 있는 아이템에 접근 하면 그 아이템의 대한 처리가 필요할 수 있다는 것을 주의하자
'''