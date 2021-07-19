"""
Stack
- 후입선출
- 스택을 이용할 때에는 별도의 라이브러리를 사용할 필요 x
"""
stack = []
stack.append(1) # push
stack.pop() # pop

print(stack) # 최하단 원소부터 출력 / first ~ last
print(stack[::-1]) # 최상단 원소부터 출력 / last ~ first

"""
Queue
- 선입선출
- 구현을 위해 deque 라이브러리 사용
"""
from collections import deque
queue = deque()
# queue = deque([3,1,4,2]) 이런식으로도 미리 정의된 queue로 초기화 가능
# queue_to_list = list(queue) -> list() 메소드를 통해 큐를 리스트 자료형으로 반환
queue.append(1) # push
queue.popleft() # pop

print(queue) # 빨리 들어온 순서대로 출력
queue.reverse() # 순서를 역순으로
print(queue) # 늦게 들어온 순서대로 출력

"""
Recursion
- 재귀함수
- 재귀식(점화식)
"""
def facorial_recursive(n):
    if n <= 1: # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n - 1)를 그대로 코드로 작성 (점화식)
    return n * facorial_recursive(n - 1)

print("5! = :", facorial_recursive(5))