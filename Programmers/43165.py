'''
- 타겟 넘버
- dfs 문제
- https://programmers.co.kr/learn/courses/30/lessons/43165
'''

def solution(numbers, target):
    global answer
    answer = 0
    def dfs(val, idx):
        global answer
        if idx == len(numbers):
            if val == target: answer += 1
        else:
            dfs(val + numbers[idx], idx + 1)
            dfs(val - numbers[idx], idx + 1)
    dfs(0, 0)
    return answer
'''
# 결론
- 전역 변수 사용하고 싶으면 전역변수를 사용할 모든 함수에 "global var_name" 해줘야함
'''