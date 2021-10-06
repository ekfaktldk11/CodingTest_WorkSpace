'''
- AC
- https://www.acmicpc.net/problem/5430
'''

# 내 풀이 (힌트 얻고 해결 ㅠ)
import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

def main():
    p = input().rstrip()
    n = int(input())
    n_ary = input().rstrip()[1:-1]
    if n > 0:
        n_ary = list(map(str, n_ary.split(',')))
    else:
        n_ary = []
    q = deque(n_ary)
    d_c = p.count('D')
    if d_c > n: return 'error'
    r_c = 0
    reverse = 1
    for oper in p:
        if oper == 'R':
            r_c += 1
        elif oper == 'D':
            try:
                if r_c % 2 == 0: q.popleft()
                else:
                    reverse *= -1
                    q.pop()
            except IndexError: return 'error'
    else:
        if r_c % 2 == 1: q.reverse()
        return "[" + ",".join(q) + "]"


for _ in range(t): print(main())

'''
# 결론
- 백준에서 기대 출력에 string 이 섞여 있으면 숫자도 string 으로 출력해야함 ..;;;
- 입력의 시간을 줄이기 위해 input = sys.stdin.readline 을 사용할때, string 입력에 대해선 input().rstrip() 을 사용해줘야함
- 만약 string 배열에 대하여 그 배열 그대로 string으로 출력하고 싶다면
    a = ['1', '2', '3']
    print("[" + ",".join(a) + "]")
- 위처럼 해야함. 코드 자체로 만보면 [,1, 2, 3] 이렇게 나올 것 같은데 그게 아님..
- 'str'.join(a) 함수는 string 형식으로 배열의 요소들을 나열해주는데 구분자를 'str' 로 하겠다는 것 임
- str1.lstrip()의 리턴 값은 str1을 lstrip()을 했을 때의 데이터를 리턴함... 즉 str1 = str1.lstrip() 이렇게 해주지 않으면 아무리 lstrip() 해줘도 그 결과가 반영되지 않음
'''