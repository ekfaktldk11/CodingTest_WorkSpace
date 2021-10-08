'''
- 숨바꼭질
- https://www.acmicpc.net/problem/1697
'''

# 내 풀이 (힌트 얻고 해결 ㅠ)
from collections import deque
n, k = map(int, input().split())
MAX = 100000
t = 0 # 시간
pos_li = [0] * (MAX + 1) # 방문한 지점을 방문하지 않도록
q = deque([(n, pos_li[n])]) # BFS 를 구현하기위한 Queue

while q:
    now, time = q.popleft()
    if now == k:
        print(time)
        break
    for i in (now + 1, now - 1, now * 2): # for 문은 이렇게도 사용이 가능하다 !
        if 0 <= i <= MAX and not pos_li[i]: # 유효한 위치내에 있으면서 방문하지 않은 곳이라면
            pos_li[i] = time + 1 # 방문한 흔적 남기기
            q.append((i, time + 1))
        else: continue

'''
# 결론
- 이러한 그래프 이론 문제 같은경우에는 visited[] 가 필요하다는 것을 잊지말자
- 이동범위가 /now + 1, now - 1, now * 2/ 로 그리 넓은 스텝이 아니라 방문한 위치를 또 방문하는 경우가 많이 있다
- 때문에 시간복잡도 & 공간복잡도(메모리)를 고려해서 방문여부와 위치의 범위를 제한시켜줘야 한다
- 문제에 주어진 조건들은 다 이유가 있다는 것을 ...
'''