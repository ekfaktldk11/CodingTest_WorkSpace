'''
- Contact
- https://www.acmicpc.net/problem/1541
'''

# re.compile()
import re
t = int(input())
for _ in range(t):
    case = re.compile('(100+1+|01)+')
    code = input()
    result = case.fullmatch(code)
    if result: print('YES')
    else: print('NO')

'''
# 결론
- 정규표현식을 이용한 문제풀이
- re.compile([문자열생성규칙])으로 해당 규칙으로 생성되는지 확인
- .match() -> 전체문자열 중 일부 문자열이 [문자열생성규칙]에 어긋나지 않으면 True를 리턴
- .fullmatch() -> 전체문자열을 대상으로 검사
'''