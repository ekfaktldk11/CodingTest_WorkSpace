'''
- 문자열 폭발
- https://www.acmicpc.net/problem/9935
'''
'''
# 내 풀이 (시간초과)
import sys
input = sys.stdin.readline
str1 = input().rstrip()
bomb = input().rstrip()

while True: O(?)
    li = str1.split(bomb)
    if str1 == li[0]: break
    str1 = ''.join(li)
if len(str1) == 0: print('FRULA')
else: print(str1)

# 접근 방법
- 매 반복마다 폭탄문자열을 기준으로 나누고 합친다
- 하지만 이 접근법은 제한시간 2초/ 문자열 길이 100만/ 폭탄문자열 길이 36/ 에서 효율적이지 못한 풀이가 됨
'''

# 해답 (힌트를 얻고 해결한 나의 풀이)
import sys
input = sys.stdin.readline
str1 = input().rstrip()
bomb = input().rstrip()
stk = []
for w in str1: # O(n) 스택에 문자 하나씩 넣으면서 넣으려는 문자가 폭탄문자열의 마지막 문자와 같으면 그 때 폭문 길이만큼 스택 꼬리 쪽을 비교하여 스택에서 빼냄
    stk.append(w)
    if w == bomb[-1]:
        try: #
            if ''.join(stk[-(len(bomb)):]) == bomb:
                for _ in range(len(bomb)): stk.pop()
        except IndexError: continue
if len(stk) == 0: print('FRULA')
else: print(''.join(stk))

'''
# 결론
- 문자열 길이는 100만이지만 폭탄문자열 길이는 36으로 비교적 크지 않다.
- 이걸 이용해서 위의 스택으로 문자열길이 백만번 만큼 one way 코드를 구현하는 접근법을 생각해낼것
'''