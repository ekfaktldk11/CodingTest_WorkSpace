"""
* 게임 개발 (난이도 '중')
- 캐릭터가 있는 장소는 1 * 1 크기의 정사각형으로 이뤄진 N * M 크기의 직사각형으로, 각각의 칸은 육지 또는 바다
- 캐릭터는 동서남북 중 한 곳을 바라봄
- 맵의 각 칸은 (A, B) 로 나타낼 수 있고, A 는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로 부터 떨어진 칸의 개수를 의미
- 캐릭터는 상하 좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 이동할 수 없음

- 캐릭터의 움직임을 설정하기 위해 정해 놓은 매뉴얼
(1). 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정함
(2). 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한칸을 전진
왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아감
(3). 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고
(1)단계로 돌아감 / 단, 이 때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춤

-입력 예시
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

-출력 예시
3
"""

"""
* 내 접근 방법
- 무식하게 모든 경우를 조건문으로 따져서 문제를 해결
- map의 복사본(visit)을 두어서 방문한 곳을 따로 check해 둠 -> map에서의 값이 0 이여도 visit의 값이 1 이면 이미 전에 방문한 경우라고 check하기 위해
- 1단계가 될 때 마다 네 방향에 대한 check를 flag로 설정하여 네 방향 모두 이동할 곳이 없을 경우로 표현 (flag > 4)
"""

"""
* 내 코드
"""
m, n = map(int, input().split())
x, y, dir = map(int, input().split())
ary = []
for i in range(m):
    temp = list(map(int, input().split()))
    ary.append(temp)

visit = ary # 방문한 곳을 check해 두기위한 map의 복사본

# 방향 순서 대로 0,1,2,3 / 북, 동, 남, 서
move = [[0,1],[1,0],[0,-1],[-1,0]]
# 이동이 끝나는 단계를 4 로 했을 때 총 1 ~ 4 단계

count = 1

flag = 1

while True: # stage 1
    if (dir == 0): dir = 3 # dir 이 0(북쪽)인 경우를 제외하고 반시계 90도를 간단히 표현가능 -> (dir - 1)
    else:
        dir = dir - i
    x_n, y_n = x + move[dir][0], y + move[dir][1]
    if(flag > 4): # 모든 방향을 다 check해도 갈곳이 없는 경우 뒤로가기
        if (dir == 1): # dir 이 1(동쪽)인경우를 제외하고 뒤로가기를 간단히 표현가능 -> (abs(dir - 2))
            x_n, y_n = x + move[3][0], y + move[3][1]
        else:
            x_n, y_n = x + move[abs(dir - 2)][0], y + move[abs(dir - 2)][1]

        if (ary[x_n][y_n] == 1): # 뒤로 가려했던 위치가 바다인 경우 루프 break
            break
        else:
            x, y = x_n, y_n
            count += 1
    elif(ary[x_n][y_n] == 1 or visit[x_n][y_n] == 1): # 왼쪽 방향이 바다이거나 이미 방문 했던 곳이라면
        flag += 1
    else: # 왼쪽 방향으로 이동가능
        visit[x_n][y_n] = 1
        x, y = x_n, y_n
        count += 1
        flag = 0

print(count)

"""
* 해답
"""
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)] # 리스트 컴프리헨션

# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x = nx - dx[direction]
            y = ny - dy[direction]
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)

"""
* 내 풀이와 해답의 풀이 방법비교
- 두 접근 모두 방문한곳을 check 하기 위한 행렬을 따로 두었다는것, brute force, 네 방향 방문에 대한 check를 flag, turn_time 을 두었다는 것
- 하지만 해답에선 외쪽으로 회전하는 코드를 함수로 두어 가독성이 좋아졌고, 방향에 대한 이동을 x,y 같이 2차원 배열로 놓은 것이 아닌 각각 따로 벡터값으로 둠
- 미세한 차이로는 방문한곳 check 행렬을 map을 복사한게 아닌 모든 요소들을 0으로 초기화했고, 뒤로 가기를 현재 위치에서 바라보고 있는 방향에으로의 이동을 - 해줌
"""

"""
* 결론
- 파이썬에서 2차원 리스트를 선언할 때는 컴프리헨션을 이용하는 것이 효율적 -> mtrx = [[0] * m for _ in range(n)] #  N * M 행렬에서
- 일반적으로 방향(direction)을 설정해서 이동하는 문제 유형에서는 dx, dy 라는 별도의 리스트를 만들어 방향을 정하는 것이 효과적
"""
