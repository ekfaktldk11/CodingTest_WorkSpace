'''
- 퇴사
- https://www.acmicpc.net/problem/14501
'''

n = int(input())
t = [] # 상담 소요시간
p = [] # 상담 수익
d = []

for i in range(n):
    a, b = map(int, input().split())
    t.append(a); p.append(b)
    d.append(b) # 최초엔 각 날의 수익은 해당 날에 상담을 수행하는 것으로 설정
d.append(0) # 마지막 날 까지 반영할 수 있도록 배열 d 에는 '0' 을 추가

for i in range(n - 1, -1, -1):
    req_t = t[i] + i
    # 상담 소요시간이 제한시간을 넘는 것은 고려해 볼 필요가 없으니
    # d[i] = d[i + 1] 로 전날에 반영했던 값으로 설정해 줌
    if req_t > n: d[i] = d[i + 1]
    else: d[i] = max(d[i + 1], p[i] + d[req_t])

print(d[0])

'''
다음의 게시물을 참고했습니다.
https://pacific-ocean.tistory.com/199
'''