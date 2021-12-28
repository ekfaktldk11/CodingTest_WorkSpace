# 피보나치 수열
# (1). 기본 재귀 소스코드
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

"""
* 위 코드는 간결 하지만 연산 속도가 너무 느림
- O(1.618..^n) .. 거의 뭐 O(2^n)
- N = 30 이면 연산횟수만 10억
"""

# (2). 메모이제이션(캐싱)(dynamic programming) 기법을 사용한 피보나치 수열 소스코드

# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100

def pibo(x):
    # 종료 조건
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라 피보나치 결과 반환
    d[x] = pibo(x - 1) + pibo(x - 2)
    return d[x]

"""
- O(n)
- 호출 순서 : pibo(5) -> p(5) p(4) p(3) p(2) p(1) p(2) p(3) 
"""